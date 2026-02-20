import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv("django_secret_key")

DEBUG = os.getenv("DEBUG", default=False)

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", default="").split(",")


# Список встроенных Django приложений
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# Список сторонних приложений
FIRST_PARTY_APPS = [
    "rest_framework",
    "captcha",
]

# Список локальных приложений
LOCAL_APPS = [
    "comments",
]

# Общий список
INSTALLED_APPS = DJANGO_APPS + FIRST_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# ДБ конфиг
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "spa_apps",
        "USER": "root",
        "PASSWORD": os.getenv("mysql_password"),
        "HOST": "127.0.0.1",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# # Редис конфиг
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/0",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         },
#     }
# }


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Настройки DRF
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 25,
    # Разрешения по умолчанию (кто может обращаться к API)
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny"  # Разрешить доступ
    ],
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",  # Ограничение запросов для анонимных пользователей
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "100/hour",  # лимит запросов для анонимных пользователей
    },
    # Рендерер — в каком формате API возвращает ответ
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",  # Рендеринг в JSON
    ],
    # Парсеры — какие типы входящих данных API умеет принимать
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",  # Принимает application/json
        "rest_framework.parsers.MultiPartParser",  # Принимает multipart/form-data
    ],
}

# Настройка cORS
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CORS_ALLOWED_ORIGINS = [  # Разрешенные источники фронтенда
        "https://localhost:3000",
        "https://127.0.0.1:3000",
    ]


# Настройка безопасности
SECURE_BROWSER_XSS_FILTER = True  # Защите от XSS
SECURE_CONTENT_TYPE_NOSNIF = True  # Запрет MIME типов
X_FRAME_OPTIONS = "DENY"  # Защите от кликджекинга


# Настройка логирования
LOGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "INFO",  # Уровень логирования
            "class": "logging.FileHandler",  # Логирование в файл
            "filename": BASE_DIR / "debug.log",  # Путь к файлу логов
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],  # Используемый обработчик
            "level": "INFO",  # уровень логирования
            "propagate": True,  # Передача логов родительским логгерам
        },
    },
}
