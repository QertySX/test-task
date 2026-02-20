# Используем официальный Python образ
FROM python:3.14-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости системы, необходимые для MySQL
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем зависимости Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем весь проект
COPY . .

# Запуск Gunicorn)
CMD ["gunicorn", "root.wsgi:application", "--bind", "0.0.0.0:8000"]