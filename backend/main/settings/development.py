from .base import *

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'food-bank',
        'USER': os.environ.get('DATABASE_USER'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}