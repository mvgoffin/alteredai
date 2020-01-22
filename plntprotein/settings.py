"""
Django settings for plntprotein project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lzonf2g-*0*244y@zh45x^jkszou13^+2bm*y)$o23kb&ur-_'

# SECURITY 'lzon%f2g-*0*244y@zh45x^jkszou13^+2bm*y)$o23kb&ur-_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# True - Env // False - Production

# TEST on MOBILE MARCO VG MAC -> ALLOWED_HOSTS = ['192.168.0.158']
ALLOWED_HOSTS = ['157.245.136.56', 'localhost', 'www.plntprotein.com', 'plntprotein.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django',
    'profiles',
    'checkout',
    'stripe',
    'users',
]
#'phonenumber_field', erase from above installed apps
#webpush gone

MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'plntprotein.urls'

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

WSGI_APPLICATION = 'plntprotein.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

if DEBUG:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'plntproteindb',
            'USER': 'plntprotein',
            'PASSWORD': 'mysql4444',
            'HOST': 'localhost',
            'PORT': '',
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

#WEBPUSH NOTIFICATIONS
WEBPUSH_SETTINGS = {
   "VAPID_PUBLIC_KEY": "BK5mWm1vcpREo7_b-Qi02dGdzjkyS7Vk0I93EPiBE2atQriPBWloxbONQnNITsMQEOENRQA1CfiN9Qi4nGiJU_4",
   "VAPID_PRIVATE_KEY": "TXjfhrDmNOuh50PmbT9rFutFNi5m_LMXaYOHyozcSxw",
   "VAPID_ADMIN_EMAIL": "marco@gubel.co.uk"
}

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
MEDIA_URL = '/media/'
#STATICFILES_DIRS = [os.path.join((BASE_DIR), 'static_in_env')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')


#BEfore DATABASE, changed for JustDjango application
#STATIC_URL = '/static/'

#if DEBUG:
#    MEDIA_URL = '/media/'
#    STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR), 'static', 'static'),
#    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_root', 'static-only', 'static')
#    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static', 'media_root')
#    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
#)


# Stripe Keys

#test keys Uncomment to go LIVE!
#STRIPE_PUBLIC_KEY = 'pk_test_BDcILuPUX13SXoMVLNxOojyt'
#STRIPE_SECRET_KEY = 'sk_test_p2vTfVUyXWWQtDTAxpP5M3Av'

#live keys
STRIPE_PUBLIC_KEY = 'pk_live_dqYcQQrsiKP9wOLLJTWnvpPc'
STRIPE_SECRET_KEY = 'sk_live_Kixpch8yverbNokj34AhO5VG'

#Django AllAuth Settings

#SENDING EMAIL NOTIFICATION NAA
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'hi@gubel.co.uk'
EMAIL_HOST_PASSWORD = 'gubel1234'
