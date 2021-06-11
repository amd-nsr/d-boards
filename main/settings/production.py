from main.settings.base import *
import os
import django_heroku
import dj_database_url
from decouple import config

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
#ALLOWED_HOSTS = ['d-boards.herokuapp.com']
ALLOWED_HOSTS = ['*']
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings.production'
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

# Static files (CSS, JavaScript, Images)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
BASE_DIR = os.path.dirname(PROJECT_ROOT)
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    #os.path.join(PROJECT_ROOT, 'static'),
    os.path.join(BASE_DIR, 'static'),
)
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

django_heroku.settings(locals())
