"""
Django settings for xwlog project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
# import configparser

from datetime import timedelta

import os

# # 读取配置文件,若没有则读取本地默认文件
# dir_project = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# conf = configparser.ConfigParser()
# ini_file_name = dir_project + '/xwlog.ini'
# # 先读取项目所在文件夹的配置文件，没有则读取默认配置
# ini_name = ini_file_name if os.path.exists(ini_file_name) else os.path.dirname(
#     os.path.abspath(__file__)) + "/default.ini"
# conf.read(ini_name)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from celery.schedules import crontab

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ijfg#govg3zk_7fphft4+k986)9zxr0lo9+zg61e#()!fdyjuh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'collection',
    'xwuser',
    'api_v1',
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

ROOT_URLCONF = 'xwlog.urls'

# 自定义后台user
AUTH_USER_MODEL = 'xwuser.MyUser'
AUTHENTICATION_BACKENDS = ['xwuser.models.MyModelBackend', 'django.contrib.auth.backends.ModelBackend']
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'static')],
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

WSGI_APPLICATION = 'xwlog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xwlog',
        'USER': 'root',
        'PASSWORD': 'Qwe@123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            "init_command": "SET foreign_key_checks = 0;",
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]

# clickhouse地址
CLICKHOUSE_ADDRESS = "localhost"
CLICKHOUSE_DATABASE = "xwtest"
CLICKHOUSE_PORT = "8123"

# mongoDB
MONGODB_ADDRESS = "localhost"
MONGODB_PORT = 27017

# celery config
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
CELERY_TIMEZONE = 'Asia/Shanghai'
# 导入任务所在文件
CELERY_IMPORTS = ("collection.tasks",)

# 需要执行任务的配置
CELERY_BEAT_SCHEDULE = {
    "test1": {
        "task": "collection.tasks.collectDataMainFunc",  # 执行的函数
        # "schedule": crontab(minute='*', hour='*', day_of_week='*', day_of_month='*', month_of_year='*'),
        'schedule': timedelta(seconds=30),
        # every minute 每分钟执行
        "args": ()  # # 任务函数参数
    },
}

# 日志配置
LOGGING = {
    'disable_existing_loggers': False,
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'ERROR',  # DEBUG message level to be written to console
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,  # this tells logger to send logging message
        },
    },
}
