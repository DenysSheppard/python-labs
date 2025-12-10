#!/bin/bash

echo "Чекаємо на готовність бази даних..."
sleep 10

python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic --noinput

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin123')" | python manage.py shell

exec python manage.py runserver 0.0.0.0:8000