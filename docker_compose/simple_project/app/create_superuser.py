import os
import django

# Указать модуль настроек вашего Django-проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '/home/artem/PycharmProjects/new_admin_panel_sprint_2/docker_compose/simple_project/app/example/settings.py')

# Инициализация Django
django.setup()

from django.contrib.auth.models import User

# Получаем данные суперпользователя из переменных окружения
username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'admin123')

# Создаём суперпользователя
try:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, password=password)
        print(f"Суперпользователь '{username}' успешно создан.")
    else:
        print(f"Суперпользователь '{username}' уже существует.")
except Exception as e:
    print(f"Ошибка при создании суперпользователя: {e}")