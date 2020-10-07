__author__ = 'Alexander'
from timi.main_settings import *
import sys

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'NAME': 'embed_system',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': '252552'
    }
}