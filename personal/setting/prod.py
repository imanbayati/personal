from personal.settings import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b!x_e2vm7)e=v(2se-mw2+pfd8megd)%3z+#%89q2n(-d=#kom'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.bayatipro.ir','bayatipro.ir']

#django sitemap
SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

X_FRAME_OPTIONS = 'SAMEORIGIN'
CSRF_COOKIE_SECURE = True
