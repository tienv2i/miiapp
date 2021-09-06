"""
Django settings for miiapp project.

Generated by 'django-admin startproject' using Django 2.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from pathlib import Path
from distutils.util import strtobool

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_DIR = Path(__file__).parent
BASE_DIR = PROJECT_DIR.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2gjn9s-9%q#n8+$@$=n%x37ww(_q+sd4scoj=y^1woaqq43&41'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(strtobool(os.getenv('DEBUG', default = 'True')))


ALLOWED_HOSTS = [os.getenv('HOST', default=''),]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webpack_loader',
    'widget_tweaks',
    'django_summernote',
    'home',
    'uploader',
    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'miiapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            PROJECT_DIR / 'templates',
        ],
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

WSGI_APPLICATION = 'miiapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB', default = 'miiapp'),
        'USER': os.getenv('POSTGRES_USER', default = 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', default = 'postgres'),
        'HOST': os.getenv('POSTGRES_HOST', default = 'postgresdb'),
        'PORT': os.getenv('POSTGRES_PORT', default = '5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'frontend' / 'dist',
    PROJECT_DIR / 'static',
    BASE_DIR / 'node_modules' / 'katex' / 'dist',
    BASE_DIR / 'frontend' / 'library'
]

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

WEBPACK_LOADER = {
    'DEFAULT': {
        'STATS_FILE': BASE_DIR / 'frontend' / 'webpack-stats.json',
    }
}
X_FRAME_OPTIONS = 'SAMEORIGIN' 

SUMMERNOTE_CONFIG = {
    'summernote': {
        'width': '100%',
        'height': '480px',
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'underline', 'clear']],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link', 'picture', 'video', 'math']],
            ['view', ['fullscreen', 'codeview', 'help' ]],
        ],
    },
    'css': (
        '/static/katex.min.css',
    ),
    'js': (
        '/static/summernote-math/summernote-math.js',
        '/static/katex.min.js'
    ),
}