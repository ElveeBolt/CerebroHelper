"""
Django settings for CerebroHelper project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1rd^zu$nt6cg0%=!umn5^!c)z7v1ef7xan1_y)fhos#!4j$50o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'mappings',
    'config'
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

ROOT_URLCONF = 'CerebroHelper.urls'

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

WSGI_APPLICATION = 'CerebroHelper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Custom settings and constants
MAPPINGS_PATH = 'main/static/main/js/mappings.json'
GENERATED_MAPPINGS = 'mappings.json'
MAPPINGS = [
    {
        'field': 'name',
        'title': 'Имя',
        'checked': 0
    },
    {
        'field': 'sex',
        'title': 'Пол',
        'checked': 0
    },
    {
        'field': 'birth_date',
        'title': 'Дата рождения',
        'checked': 0
    },
    {
        'field': 'birth_place',
        'title': 'Место рождения',
        'checked': 0
    },
    {
        'field': 'country',
        'title': 'Страна',
        'checked': 0
    },
    {
        'field': 'address',
        'title': 'Адрес',
        'checked': 0
    },
    {
        'field': 'relationship',
        'title': 'Статус отношений',
        'checked': 0
    },
    {
        'field': 'childrens',
        'title': 'Дети',
        'checked': 0
    },
    {
        'field': 'phones',
        'title': 'Телефон(-ы)',
        'checked': 0
    },
    {
        'field': 'emails',
        'title': 'E-mails',
        'checked': 0
    },
    {
        'field': 'socials',
        'title': 'Социальные сети',
        'checked': 0
    },
    {
        'field': 'educations',
        'title': 'Образование',
        'checked': 0
    },
    {
        'field': 'works',
        'title': 'Работа',
        'checked': 0
    },
    {
        'field': 'documents',
        'title': 'Документы',
        'checked': 0
    },
    {
        'field': 'cars_status',
        'title': 'Наличие авто',
        'checked': 0
    },
    {
        'field': 'cars',
        'title': 'Авто',
        'checked': 0
    },
    {
        'field': 'banks',
        'title': 'Платежные системы и банки',
        'checked': 0
    },
    {
        'field': 'ownerships',
        'title': 'Собственность',
        'checked': 0
    },
    {
        'field': 'links',
        'title': 'Ссылки',
        'checked': 0
    },
    {
        'field': 'accounts',
        'title': 'Аккаунты',
        'checked': 0
    },
    {
        'field': 'ip',
        'title': 'IP',
        'checked': 0
    },
    {
        'field': 'coordinates',
        'title': 'Координаты',
        'checked': 0
    },
    {
        'field': 'comment',
        'title': 'Комментарий',
        'checked': 0
    },
    {
        'field': 'database',
        'title': 'База данных',
        'checked': 1
    },
    {
        'field': 'status',
        'title': 'Статус',
        'checked': 1
    },
    {
        'field': 'category',
        'title': 'Категория',
        'checked': 1
    },
    {
        'field': 'tags',
        'title': 'Теги',
        'checked': 0
    },
    {
        'field': 'date',
        'title': 'Дата',
        'checked': 1
    }
]

GENERETED_CONFIG = 'config.json'