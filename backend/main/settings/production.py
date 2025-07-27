from .base import *

# Turns off the warning that tells you it's not a production server
os.environ["DJANGO_RUNSERVER_HIDE_WARNING"] = "true"

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']