"""
Django settings for LetAndrewCook project.

Generated by 'django-admin startproject' using Django 4.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
SECURE_SSL_REDIRECT = os.getenv('SSL_REDIRECT', 'False').lower() == 'true'
SECURE_SSL_HOST="https://www.letandrewcook.com:443"
PREPEND_WWW = os.getenv('PREPEND_WWW', default=False)
BASE_URL = os.getenv('BASE_URL', 'False').lower() == 'true'

ALLOWED_HOSTS =os.getenv('ALLOWED_HOSTS').split(",")


# Application definition

INSTALLED_APPS = [
    'tictactoe_app',
    'website.apps.WebsiteConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mod_wsgi.server',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LetAndrewCook.urls'

CSRF_TRUSTED_ORIGINS = ["https://letandrewcook.com", "https://www.letandrewcook.com"]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LetAndrewCook.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DATABASE_ROUTERS = ["LetAndrewCook.router.MyRouter"]

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = BASE_DIR / 'staticfiles'

# The URL to use when referring to static files (where they will be served from)
STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# email
DEFAULT_FROM_EMAIL = "andrew@letandrewcook.com"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"  # new
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_HOST_USER = 'andrew@letandrewcook.com'
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# https://docs.djangoproject.com/en/4.2/topics/cache/
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "my_cache_table",
        "TIMEOUT": 60 * 60 * 12,
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(os.path.dirname(__file__), 'error.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'ERROR',  # Logs only errors and critical issues
            'propagate': True,
        },
    },
}

