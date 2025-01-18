#!/bin/sh

# Включаем режим "выход при ошибке"
set -e

# Ожидание доступности базы данных
dockerize -wait tcp://theatre-db:5432 -timeout 30s

# Выполнение миграций базы данных
python manage.py migrate

# Выполняем сбор статических файлов
python manage.py collectstatic --noinput

# Создание суперпользователя (если его ещё нет)
python create_superuser.py

# Запуск uWSGI с использованием конфигурационного файла uwsgi.ini
uwsgi --ini uwsgi.ini