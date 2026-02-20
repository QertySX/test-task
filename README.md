Test Task — Django Rest Framework + MySQL 

Стек технологий

- Python 3.12+

- Django

- MySQL 8

- Docker

- Docker Compose

Описание

- Возвращает список всех комментариев верхнего уровня
- Поддерживается пагинация
- Поддерживается сортировка по: username, email, created_at

Быстрый старт

- git clone https://github.com/QertySX/test_task.git
- cd test_task

- cp .env.example .env

- Пример .env

django_secret_key ='Ваш секретный ключ' 

NAME='Ваше имя бд'
HOST='127.0.0.1'
mysql_password='Ваш пароль'

DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

- DJANGO_SECRET_KEY можно сгенерировать через Python

from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())

Сборка и запуск контейнеров

- docker compose up --build


Применение миграций

- docker compose exec web python manage.py migrate

Переходим по url в браузере или Postman

- http://127.0.0.1:8000/api/v1/comments/


