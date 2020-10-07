"""
WSGI config for timi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from timi.main_settings import WHICH

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "timi.settings.{}".format(WHICH))

application = get_wsgi_application()
