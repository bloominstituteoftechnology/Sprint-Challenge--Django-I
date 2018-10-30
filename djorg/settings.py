from decouple import config
import dj_database_url

ALLOWED_HOSTS = []

ROOT_URLCONF = 'djorg.urls'

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', cast=bool)

# DATABASES['default'] = dj_database_url.config(conn_max_age=600)
# DATABASES['default'] = dj_database_url.config(default='postgres://...')
DATABASES['default'] = dj_database_url.parse('postgres://...', conn_max_age=600)

MIDDLEWARE = [
  # 'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
  # ...
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')