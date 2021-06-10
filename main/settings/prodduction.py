from main.settings.base import *
import django_heroku
import dj_database_url
from decouple import config

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = ['0.0.0.0', 'localhost']
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings.production'

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}