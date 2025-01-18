#!/bin/sh

# Выполнить миграции
python3 manage.py migrate

# Собрать статические файлы
python3 manage.py collectstatic --noinput

# Создать суперпользователя, если указаны переменные окружения
if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
    python3 manage.py createsuperuser --noinput
fi

# Запустить uwsgi
uwsgi --ini uwsgi.ini