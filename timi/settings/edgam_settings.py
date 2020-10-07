from timi.main_settings import *

DEBUG = True

ALLOWED_HOSTS = ['.embed-systems.com']

SESSION_COOKIE_DOMAIN = '.embed-systems.com'

DATABASES = {
    'default': {
        'NAME': 'embed_system',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': ''
    }
}
