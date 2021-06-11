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