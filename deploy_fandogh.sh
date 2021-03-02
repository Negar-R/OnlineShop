#!/bin/sh
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py loaddata fixtures/*.json
gunicorn OnlineShopProject.wsgi:application -b 0.0.0.0:80