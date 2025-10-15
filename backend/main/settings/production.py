from .base import *

# Turns off the warning that tells you it's not a production server
os.environ["DJANGO_RUNSERVER_HIDE_WARNING"] = "true"

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'food-bank',
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}