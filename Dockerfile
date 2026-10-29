
# Базовый образ Python
FROM python:3.12-slim

# Рабочая папка внутри контейнера
WORKDIR /app

# Настройки Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем Flask и другие библиотеки
RUN pip install --no-cache-dir -r requirements.txt

# Копируем серверное приложение
COPY app.py .

# Внутренний порт Flask
EXPOSE 5001

# Запуск сервера внутри контейнера
CMD ["python", "-m", "flask", "--app", "app:app", "run", "--host=0.0.0.0", "--port=5001"]
