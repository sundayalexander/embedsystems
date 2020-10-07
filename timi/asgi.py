__author__ = 'Edward'

"""
ASGI config for timi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

import django
from channels.routing import get_default_application

from timi.main_settings import WHICH

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'timi.settings.{}'.format(WHICH))

django.setup()
application = get_default_application()
