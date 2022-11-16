from onlyildiz.settings.base import *

DEBUG = False

ALLOWED_HOSTS = [
     "onlyildiz.com","www.onlyildiz.com"
]

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'onlyildiz',
        'USER': 'quluquliyev',
        'PASSWORD': 'xsaq005500',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
