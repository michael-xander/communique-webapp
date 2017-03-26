# This file contains settings for the production environment

from .base_settings import *

import os

DEBUG = False

# reading the FCM server key
ENV_FCM_SERVER_KEY = os.environ['FCM_SERVER_KEY']
FCM_DJANGO_SETTINGS = {
    "FCM_SERVER_KEY": ENV_FCM_SERVER_KEY
}

# read the security key from the environment
SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
