FROM python:3.10

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE example.settings
ENV DOCKERIZE_VERSION v0.6.1

# Копируем необходимые файлы
COPY run_uwsgi.sh run_uwsgi.sh
COPY requirements.txt requirements.txt
COPY uwsgi/uwsgi.ini uwsgi.ini

# Создаём директории
RUN mkdir -p /var/www/static /var/www/media /opt/app/static /opt/app/media

# Установка wget и ca-certificates для загрузки Dockerize
RUN apt-get update && apt-get install -y wget ca-certificates

RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем проект
COPY . .

# Копируем скрипт entrypoint
COPY entrypoint.sh /opt/app/entrypoint.sh

EXPOSE 8000

# Проверка состояния контейнера
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s \
    CMD curl -f http://localhost:8000/ || exit 1

RUN chmod +x entrypoint.sh

# Указываем скрипт как точку входа
ENTRYPOINT ["sh", "/opt/app/entrypoint.sh"]


