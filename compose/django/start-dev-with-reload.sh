#!/bin/sh
python manage.py migrate
gunicorn --reload app:app --bind 0.0.0.0:8000
