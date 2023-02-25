from decouple import config

from .base import *

SECRET_KEY = config("SECRET_KEY_DEV")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
