#!/bin/bash
python manage.py makemigrations simple_authentication --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
exec "$@"