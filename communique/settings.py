# This file contains settings for the production environment
from .base_settings import *

import dj_database_url

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f8i039#2fq#1@27u-l$#s(#!=(ir52nq77cffsa10q)jbr_2im'

ALLOWED_HOSTS = ['*']

DATABASES = {}
DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
