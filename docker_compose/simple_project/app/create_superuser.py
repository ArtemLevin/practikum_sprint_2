from django.contrib.auth.models import User
import os

username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'admin123')

try:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, password=password)
        print(f"Суперпользователь '{username}' успешно создан.")
    else:
        print(f"Суперпользователь '{username}' уже существует.")
except Exception as e:
    print(f"Ошибка при создании суперпользователя: {e}")