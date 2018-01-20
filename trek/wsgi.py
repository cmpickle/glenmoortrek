"""
WSGI config for trek project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import logging

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trek.settings")

from whitenoise.django import DjangoWhiteNoise

logger = logging.getLogger('herokulogger')
logger.info('Starting applicatoin')

application = get_wsgi_application()
application = DjangoWhiteNoise(application)