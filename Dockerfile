# Используем официальный Python образ
FROM python:3.14-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    build-essential \          
    default-libmysqlclient-dev \ 
    pkg-config \             
    libssl-dev \             
    libffi-dev \          
    python3-dev \            
    git \               
    curl \                  
    locales \                
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем зависимости Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем весь проект
COPY . .

# Запуск Gunicorn)
CMD ["gunicorn", "root.wsgi:application", "--bind", "0.0.0.0:8000"]