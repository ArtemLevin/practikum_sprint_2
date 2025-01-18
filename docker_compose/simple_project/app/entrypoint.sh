#!/bin/sh

# Выполнить миграции
python3 manage.py migrate

# Собрать статические файлы
python3 manage.py collectstatic --noinput

# Создать суперпользователя, если указаны переменные окружения
if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
    python3 create_superuser.py
fi

# Запустить uwsgi
uwsgi --ini uwsgi.ini