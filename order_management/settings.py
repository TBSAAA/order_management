"""
Django settings for order_management project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y&3h!#^6&#^pcjn%-nch++i8uw_5d*^_6*b^-2!0p#u6if_3*m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    'django.contrib.staticfiles',
    'web.apps.WebConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middle_ware.Permissions.Authority'
]

ROOT_URLCONF = 'order_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                # 'django.contrib.auth.context_processors.auth',
                # 'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'order_management.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = 'media/'
MEDIA_ROOT = Path(__file__).resolve().parent.parent.parent / 'media'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# local settings
try:
    from .local_settings import *
except ImportError:
    pass

# session config
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7  # 7 days

# define user session key
ORDER_USER_SESSION = 'user_info'

# urls config
INDEX_URL = "/index"
WHITE_LIST_URL = ['/login/', '/get_code/', '/register/', '/login_with_code/', '/', '/study/experience/']
LOGIN_URL = "/login"
HOME_URL = "/home"

# dynamic menu config
MENU_LIST = {
    "ADMIN": [
        {
            "title": "User Management",
            "icon": "uil uil-users-alt",
            "children": [
                {"title": "user list", "url": "/user/list/", "name": "user_list"},
                {"title": "level management", "url": "/level/list/", "name": "level_list"},
                {"title": "Price Strategy", "url": "/product/list", "name": "price_list"},
            ]
        },
        {
            "title": "Order",
            "icon": "uil uil-users-alt",
            "children": [
                {"title": "order List", "url": "/order/list/", "name": "order_list"},
            ]
        },
        {
            "title": "Commodity",
            "icon": "uil uil-users-alt",
            "children": [
                {"title": "product list", "url": "/product/list/", "name": "product_list"},
            ]
        },
    ],
    "USER": [
        {
            "title": "Order center",
            "icon": "uil uil-users-alt",
            "children": [
                {"title": "order management", "url": "/order/list/", "name": "user_order_list"},
                {"title": "transaction record", "url": "/order/add/", "name": "user_transaction_list"},
            ]
        },
    ],
}

# permissions config
PUBLIC_PERMISSION = {
    "home": {"title": "home", 'parent': None},
    "logout": {"title": "logout", 'parent': None},
}

PERMISSION_LIST = {
    "ADMIN": {
        "user_list": {"title": "user list", 'parent': None},
        "user_add": {"title": "user add", 'parent': "user_list"},
        "user_edit": {"title": "user edit", 'parent': "user_list"},
        "user_delete": {"title": "user del", 'parent': "user_list"},

        "level_list": {"title": "level management", 'parent': None},
        "level_add": {"title": "level add", 'parent': "level_list"},
        "level_edit": {"title": "level edit", 'parent': "level_list"},
        "level_delete": {"title": "level del", 'parent': "level_list"},

        "price_list": {"title": "price strategy", 'parent': None},
        "price_add": {"title": "price add", 'parent': "price_list"},
        "price_edit": {"title": "price edit", 'parent': "price_list"},
        "price_delete": {"title": "price del", 'parent': "price_list"},

        "order_list": {"title": "order list", 'parent': None},
        "order_add": {"title": "order add", 'parent': "order_list"},
        "order_edit": {"title": "order edit", 'parent': "order_list"},
        "order_delete": {"title": "order del", 'parent': "order_list"},

        "product_list": {"title": "product list", 'parent': None},
        "product_add": {"title": "product add", 'parent': "product_list"},
        "product_edit": {"title": "product edit", 'parent': "product_list"},
        "product_delete": {"title": "product del", 'parent': "product_list"},

    },
    "USER": {
        "user_order_list": {"text": "order management", 'parent': None},

        "user_transaction_list": {"text": "transaction record", 'parent': None},

    }
}
