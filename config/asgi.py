import os
from channels.asgi import get_channel_layer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.production")
# TODO: Might need to port things from wsgi.py here
# or adapt things there, I don't know.
channel_layer = get_channel_layer()
