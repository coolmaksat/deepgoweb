"""
Django settings for deepgoweb project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import sys
from configurations import Configuration
from kombu import Exchange, Queue

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)


sys.path.insert(0, rel('apps'))


class BaseConfiguration(Configuration):
    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '7#14#$%o01-7&t!4dx7tt)b=me!r397n3%8+s*^5eq331-zxqv'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = ['*']

    ADMINS = [('Maxat Kulmanov', 'coolmaksat@gmail.com'), ]

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'accounts',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'deepgo',
        'widget_tweaks',
        'rest_framework',
    ]

    MIDDLEWARE_CLASSES = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'deepgoweb.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [rel('templates')],
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

    WSGI_APPLICATION = 'deepgoweb.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/1.9/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'deepgoweb',
            'HOST': 'localhost',
            'USER': 'postgres',
            'PASSWORD': '111'
        }
    }

    # Memcached
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }

    SESSION_ENGINE = "django.contrib.sessions.backends.cache"

    TEST_RUNNER = 'django.test.runner.DiscoverRunner'

    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

    # Password validation
    # https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/1.9/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.9/howto/static-files/

    STATIC_URL = '/static/'
    STATIC_ROOT = 'deepgoweb/public'
    MEDIA_ROOT = 'deepgoweb/media'
    MEDIA_URL = '/media/'

    # User profile module
    AUTH_PROFILE_MODULE = 'accounts.models.UserProfile'

    STATICFILES_DIRS = (
        rel('static'),)

    SITE_ID = 1
    SITE_DOMAIN = 'localhost:8000'

    # Celery configuration
    RABBIT_HOST = 'localhost'
    RABBIT_PORT = 5672

    CELERY_BROKER_URL = 'pyamqp://{user}:{pwd}@{host}:{port}//'.format(
        user=os.environ.get('RABBIT_USER', 'guest'),
        pwd=os.environ.get('RABBIT_PASSWORD', 'guest'),
        host=RABBIT_HOST,
        port=RABBIT_PORT)

    CELERY_RESULT_BACKEND = 'rpc://'
    CELERY_WORKER_CONCURRENCY = 1
    CELERY_BROKER_POOL_LIMIT = 1
    CELERY_BROKER_CONNECTION_TIMEOUT = 10

    # configure queues, currently we have only one
    CELERY_DEFAULT_QUEUE = 'default'
    CELERY_QUEUES = (
        Queue('default', Exchange('default'), routing_key='default'),
    )

    # Sensible settings for celery
    CELERY_ALWAYS_EAGER = False
    CELERY_ACKS_LATE = True
    CELERY_TASK_PUBLISH_RETRY = True
    CELERY_DISABLE_RATE_LIMITS = False

    # By default we will ignore result
    # If you want to see results and try out tasks interactively, change it to False
    # Or change this setting on tasks level
    CELERY_IGNORE_RESULT = True
    CELERY_SEND_TASK_ERROR_EMAILS = False
    CELERY_TASK_RESULT_EXPIRES = 600


class Development(BaseConfiguration):
    pass

class Production(BaseConfiguration):
    DEBUG = False

