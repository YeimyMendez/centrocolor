"""
Django settings for CentroColor project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k4@-0kge7rqv68)6qv4p)4y3%@h9z^hcrul3opgae3p#=&g_x)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# LOCAL
ALLOWED_HOSTS = []

# HEROKU
# ALLOWED_HOSTS = ['centrocolor.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'principal',
    'crispy_forms',
    'webservices',
    'rest_framework',
    'gunicorn',
    'psycopg2',
]

# Config Crispy_forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CentroColor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],#llamado e templates
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

WSGI_APPLICATION = 'CentroColor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# # LOCAL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#HEROKU
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'd61ai98csvm0lf',
#         'USER': 'qtltvtzfyurfug',
#         'PASSWORD': '5cfbcd76bf610c3733a744f2241ddf872fc2bc5501316f60b021562044696ad5',
#         'HOST': 'ec2-44-209-24-62.compute-1.amazonaws.com',
#         'PORT': '5432',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

# AUTH_USER_MODEL = 'principal.Usuario'

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

#ESTATIC PRUEBA LOCAL
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'principal/static'),)
STATIC_ROOT = '/principal/static'

# HEROKU
# STATIC_URL = '/static/'
# STATIC_ROOT = "static"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
