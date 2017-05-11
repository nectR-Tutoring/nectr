#!/bin/sh
python /app/manage.py collectstatic --noinput
daphne config.asgi:channel_layer -u /tmp/daphne.sock
python manage.py runworker
