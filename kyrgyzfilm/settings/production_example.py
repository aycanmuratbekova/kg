from .base import *


SECRET_KEY = 'django-insecure-&i=43ubtzl$hb278p$o)#!r2gbyy8amk39p_hikv9w2ghi$$$x'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = ["localhost", "192.168.0.1"]
