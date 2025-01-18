FROM python:3.10

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE example.settings

# Копируем необходимые файлы
COPY run_uwsgi.sh run_uwsgi.sh
COPY requirements.txt requirements.txt
COPY uwsgi/uwsgi.ini uwsgi.ini

# Создаём директории
RUN mkdir -p /var/www/static /var/www/media /opt/app/static /opt/app/media

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем проект
COPY . .

EXPOSE 8000

# Проверка состояния контейнера
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s \
    CMD curl -f http://localhost:8000/ || exit 1

CMD ["sh", "-c", "python manage.py migrate &&
                  python manage.py collectstatic --noinput &&
                  if [ \"$DJANGO_SUPERUSER_USERNAME\" ]; then python manage.py createsuperuser --noinput; fi &&
                  uwsgi --ini uwsgi.ini"]