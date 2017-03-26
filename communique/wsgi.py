"""
WSGI config for communique project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

# check for specified settings module (for prod settings) and utilise dev settings if not found
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "communique.dev_settings")
