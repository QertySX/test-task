# Содержит представления для обработки запросов API

from rest_framework import exceptions, status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter

from .models import Comment
from .serializers import CheckCaptchaSerializer, CommentsSerializer


class CommentsListAPIView(ListAPIView):
    # Обработка GET запроса с пагинацией
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    pagination_class = PageNumberPagination
    filter_backends = [OrderingFilter]

    ordering_fields = ["username", "email", "created_at"]
    ordering = ["-created_at"]

    def get_queryset(self):
        # Доп. фильтрация
        return Comment.objects.filter(parent__isnull=True)

    def post(self, request):
        # Обработка POST запроса с капчей
        captcha_serializer = CheckCaptchaSerializer(data=request.data)
        if not captcha_serializer.is_valid():
            raise exceptions.ValidationError({"error": "Invalid CAPTCHA"})

        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
