# Dockerfile
FROM python:3.9

# Установите рабочую директорию
WORKDIR /app

# Копируйте файлы проекта в контейнер
COPY requirements.txt ./
COPY ./db ./db
COPY ./api.py ./

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Запустите приложение
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
