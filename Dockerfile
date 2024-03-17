# Docker-команда FROM вказує базовий образ контейнера
# Наш базовий образ - це Linux з попередньо встановленим python-3.11
FROM python:3.11


# Встановимо робочу директорію всередині контейнера
WORKDIR .

# Скопіюємо інші файли в робочу директорію контейнера
COPY . .

# Встановимо залежності всередині контейнера
RUN pip install -r requirements.txt

# Позначимо порт, де працює застосунок всередині контейнера
EXPOSE 5432

# Запустимо наш застосунок всередині контейнера
ENTRYPOINT ["python", "main.py"]

# Cоздать том при запуске контейнера
VOLUME /storage/data.json