from main.settings.base import *


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

SECRET_KEY = 'django-insecure--iradtdx(kuq-4&+m(mu89+xc+xr1=(dwz=t$ln#ncj(e(7v5b'
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configure the STATIC-related parameters
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]