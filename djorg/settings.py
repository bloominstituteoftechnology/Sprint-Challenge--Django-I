import os,dj_database_url
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MIDDLEWARE = [
  'whitenoise.middleware.WhiteNoiseMiddleware',
]

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG',cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS')