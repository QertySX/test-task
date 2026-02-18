# Сериализаторы для модели Comments

import re
import sys
from io import BytesIO

import bleach
from captcha.serializers import CaptchaSerializer
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Comment

ALLOWED_TAGS = ["a", "code", "i", "strong"]
ALLOWED_ATTRIBUTES = {"a": ["href", "title"]}


class CommentsSerializer(serializers.ModelSerializer):
    # Базовый сериализатор для модели Comment
    class Meta:
        model = Comment
        fields = [
            "id",
            "parent",
            "username",
            "email",
            "homepage",
            "text",
            "image",
            "file",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def validate_username(self, value):
        # только латиница и цифры
        if not re.match(r"^[a-zA-Z0-9]+$", value):
            raise serializers.ValidationError(
                "Username может содержать только латинские буквы и цифры"
            )
        return value

    def validate_text(self, value):
        # очистка текста от запрещённых тегов
        cleaned = bleach.clean(
            value, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES, strip=True
        )
        return cleaned

    def validate_file(self, value):
        # Проверка размера
        max_size = 100 * 1024
        if value.size > max_size:
            raise serializers.ValidationError("Файл слишком большой")

        if value.content_type != "text/plain":
            raise serializers.ValidationError(
                "Разрешены только текстовые файлы (MIME: text/plain)."
            )

        return value

    def validate_image(self, value):
        if not value:
            return value

        try:
            img = Image.open(value)
        except Exception:
            raise serializers.ValidationError("Некорректное изображение")

        if img.format not in ["JPEG", "PNG", "GIF"]:
            raise serializers.ValidationError("Допустимые форматы: JPG, PNG, GIF")

        max_width, max_height = 320, 240

        if img.width > max_width or img.height > max_height:
            img.thumbnail((max_width, max_height), Image.LANCZOS)

            buffer = BytesIO()
            format = img.format
            img.save(buffer, format=format)
            buffer.seek(0)

            return InMemoryUploadedFile(
                buffer,
                field_name="image",
                name=value.name,
                content_type=value.content_type,
                size=buffer.tell(),
                charset=None,
            )
        return value


class CheckCaptchaSerializer(CaptchaSerializer):
    pass
