# -*- coding: utf-8 -*-

"""
Django settings for guizi project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public/media/')
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static/'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fgvk_06s72**4r7k%7i-@(xe9p-uk+ltcb8jb**s!lwh2olxvz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Add the Guardian and userena authentication backends
AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

SITE_ID = 1


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.sites',
    'django_comments',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'filer',
    'mptt',
    'taggit',
    'haystack',
    # 'tastypie',
    'guardian',
    'userena',
    'easy_thumbnails',
    'core',
    'profile',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    # 'django.middleware.cache.CacheMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'userena.middleware.UserenaLocaleMiddleware',
    'django.middleware.gzip.GZipMiddleware',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        # 'LOCATION': '/var/tmp/django_cache',
        # 'TIMEOUT': 600,
        # 'OPTIONS': {
        #     'MAX_ENTRIES': 1000
        # }
    }
}

ROOT_URLCONF = 'guizi.urls'

#for the django-filer image management
THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
#end

# Settings used by Userena
LOGIN_REDIRECT_URL = '/user/%(username)s/'
LOGIN_URL = '/user/signin/'
LOGOUT_URL = '/user/signout/'
AUTH_PROFILE_MODULE = 'profile.Profile'
USERENA_SIGNIN_REDIRECT_URL = '/'
USERENA_ACTIVATION_REQUIRED = False
USERENA_DISABLE_PROFILE_LIST = True
USERENA_MUGSHOT_SIZE = 140
USERENA_MUGSHOT_GRAVATAR = False
USERENA_MUGSHOT_DEFAULT="http://img2.duitang.com/uploads/item/201207/22/20120722225459_RKAmM.jpeg"


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'guizi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'private/development.db'),
    }
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'core.searchengin.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(PROJECT_ROOT, 'whoosh_index'),
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-CN'
ugettext = lambda s: s
LANGUAGES = (
    ('zh', ugettext('zh_CN')),
)


TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

THUMBNAIL_ROOT = "uploads/thumbnails"
UPLOAD_TO = "uploads"
THUMBNAIL_SIZE = 400

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}

# Needed for Django guardian
ANONYMOUS_USER_ID = -1

#The default format of tastypie of RESTFUL
TASTYPIE_DEFAULT_FORMATS = ['json']