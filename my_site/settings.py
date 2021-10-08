"""
Django settings for my_site project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
# environmnet variable are simply global variables.
from os import getenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# the secret key is used internally by django -
# - for asigning cookies and for security aspects in gerneral.
# getenv("SECRET_KEY")
SECRET_KEY = 'django-insecure-s$^tz@jpm!c*zbbqs8&*eo%-)hhdl4fo$g3oh*n$6dj-l!sk20'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv("IS_DEVELOPMENT", True)

ALLOWED_HOSTS = [
    getenv("APP_HOST", "127.0.0.1")
]


# Application definition

INSTALLED_APPS = [
    'blog',
    'storages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'my_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates"
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

WSGI_APPLICATION = 'my_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'djangoblog',
        "PASSWORD": 'djangoblog',
        'HOST': 'django-blog.c6h7zbziuf0m.us-east-2.rds.amazonaws.com',
        "PORT": '5432'

    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_ROOT wil automatically collect all the static files from the different parts of our project,
# - and automatically move them into the folder here then.
# before we deploy we should collect all our static files.
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

MEDIA_ROOT = BASE_DIR / "uploads"
MEDIA_URL = "/files/"

# we need to add a couple of AWS specific settings which will be picked up soon by the boto3 package - 
# - to tell Django and python how to communicate with our AWS account.
AWS_STORAGE_BUCKET_NAME = "django-blog-by-justin"
AWS_S3_REGION_NAME = "us-east-2"
AWS_ACCESS_KEY_ID = "AKIATWVFOWI7IN4CDU6L"
AWS_SECRET_ACCESS_KEY = "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"
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

# static's folder name is up to us, a folder which will be created in our S3 bucket -
# - automatically once we collect all static files.
STATICFILES_FOLDER = "static"
MEDIAFILES_FOLDER = "media"


# Default: 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATICFILES_STORAGE = "custom_storages.StaticFileStorage"
# works for media files.
DEFAULT_FILE_STORAGE = "custom_storages.MediaFileStorage"


