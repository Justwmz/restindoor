"""
Django settings for restindoor project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dil%45r7f-e&l_!z_gt+ud!6p1@2z-ta@!fm_y*!$ojnnvt8*r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jquery',
    'djangoformsetjs',
    'floppyforms',
    'haystack',
    'index',
    'client',
    'restaurant',
    'tech',
    'analytics',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'restindoor.urls'

WSGI_APPLICATION = 'restindoor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'restindoor',
        'USER': 'restindoor',
        'PASSWORD': 'restindoor',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'


# Admins

ADMINS = (
    ('Admin', 'a.blakov@restindoor.com.ua'),
)
MANAGERS = ADMINS


# Emailing

EMAIL_HOST = 'server.restindoor.com.ua'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'crm@restindoor.com.ua'
EMAIL_HOST_PASSWORD = 'qKZkPgHARJ'
DEFAULT_FROM_EMAIL = 'crm@restindoor.com.ua'


# Login

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'


# Templates

TEMPLATE_DIRS = os.path.join(BASE_DIR, "templates")


# Search backend

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8080/solr'
    },
}
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_DEFAULT_OPERATOR = 'OR'
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
