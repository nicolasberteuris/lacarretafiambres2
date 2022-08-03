from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['lacarreta.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd5ihke15eofqto',
        'USER': 'fiqyxxcrmbreip',
        'PASSWORD': '7ea5a82fcbe452abd8c1d21254d4a8e3875c89f1a14533cba38c3d0c58bf2b6c',
        'HOST': 'ec2-54-159-22-90.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')

