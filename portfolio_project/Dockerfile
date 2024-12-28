# Используем базовый образ Python
FROM python:3.10-slim

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Копирование файла зависимостей
COPY requirements.txt .

# Установка зависимостей проекта
RUN pip install --no-cache-dir -r requirements.txt

# Копирование всего проекта в контейнер
COPY . .

# Указание открытого порта для приложения
EXPOSE 8000

# Команда запуска приложения с использованием Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "portfolio_project.wsgi:application"]
