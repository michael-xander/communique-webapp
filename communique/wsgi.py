"""
WSGI config for communique project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# imports specific to heroku deployment
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "communique.settings")

application = get_wsgi_application()
# command specific to Heroku
application = DjangoWhiteNoise(application)
