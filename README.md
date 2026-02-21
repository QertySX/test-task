

# Test Task - Django REST Framework + MySQL

## Стек технологий

* Python 3.12+
* Django
* MySQL 8
* Docker
* Docker Compose

---

## Описание проекта

Проект предоставляет API для работы с комментариями:

* Возвращает список всех комментариев верхнего уровня
* Поддерживает пагинацию
* Поддерживает сортировку по полям: `username`, `email`, `created_at`

---

## Быстрый старт

1. Клонируем репозиторий:

```bash
git clone https://github.com/QertySX/test-task.git
cd test-task
```

2. Создаём файл окружения:

```bash
cp .env.example .env
```

3. Пример содержимого `.env`:

```env
DJANGO_SECRET_KEY='ваш_секретный_ключ'
NAME='имя_бд'
HOST='127.0.0.1'
MYSQL_PASSWORD='ваш_пароль'
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

> секретный ключ можно сгенерировать в Python:

```
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

---

## Сборка и запуск контейнеров

### Для Docker Compose v2 (плагин):

```bash
docker compose build
docker compose up
```

### Для старого docker-compose:

```bash
docker-compose build
docker-compose up
```

---

## Применение миграций

```bash
docker compose exec web python manage.py migrate
```

---

## Тестирование API

После запуска контейнеров, API доступно по адресу:

```
http://127.0.0.1:8000/api/v1/comments/
```

Можно использовать **Postman**, **curl** или браузер.

---

