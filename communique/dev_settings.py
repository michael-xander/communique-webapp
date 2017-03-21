# This file contains settings for the development environment
from .base_settings import *

FCM_DJANGO_SETTINGS = {
    "FCM_SERVER_KEY": "AIzaSyBI2HmSj0ir_h4XFzOQlW99M1YRVdOU41s"
}

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
