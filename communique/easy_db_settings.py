# This file contains settings for the test environment
from .base_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f8i039#2fq#1@27u-l$#s(#!=(ir52nq77cffsa10q)jbr_2im'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
