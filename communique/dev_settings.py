# This file contains settings for the development environment
from .base_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f8i039#2fq#1@27u-l$#s(#!=(ir52nq77cffsa10q)jbr_2im'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'communique_database',
        'USER': 'communique_user',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'',
    }
}
