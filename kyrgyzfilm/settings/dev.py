from .base import *


SECRET_KEY = '00x3jg)l$edpph@24_2pkxermfyb&1=k!m@c6#tgd(j8nza04g'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}