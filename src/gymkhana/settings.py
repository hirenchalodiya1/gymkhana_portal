"""
Django settings for gymkhana project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', cast=str)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

HTML_MINIFY = not DEBUG

MAINTENANCE_MODE = config('MAINTENANCE_MODE', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'social_django',
    'graphene_django',
    'rest_framework',
    'versatileimagefield',
    'photologue',
    'sortedm2m',
    'ckeditor',
    'ckeditor_uploader',
    'corsheaders',
    'hitcount',
    'django_cleanup',
    'oauth.apps.OauthConfig',
    'main.apps.MainConfig',
    'forum.apps.ForumConfig',
    'events.apps.EventsConfig',
    'gallery.apps.GalleryConfig',
    'news.apps.NewsConfig',
    'konnekt.apps.KonnektConfig',
    'festivals.apps.FestivalsConfig',
    'fixture.apps.FixtureConfig'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware'
]

SITE_ID = 1

ROOT_URLCONF = 'gymkhana.urls'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, config('STATIC_PATH', default='../staticfiles', cast=str))

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, config('MEDIA_PATH', default='../media', cast=str))

MEDIA_URL = '/media/'

CUSTOM_TEMPLATE_DIR_NAME = 'html_templates'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(MEDIA_ROOT, CUSTOM_TEMPLATE_DIR_NAME)
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gymkhana.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

if config('SQLITE_DB', cast=bool, default=False):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

LOGIN_REDIRECT_URL = 'oauth:session'

LOGIN_URL = 'login'

LOGIN_ERROR_URL = '/login'

SOCIAL_AUTH_LOGIN_ERROR_URL = '/login'
SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['to']

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# Social Auth settings
SOCIAL_AUTH_CLEAN_USERNAMES = True

SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS = ['iitj.ac.in']

SOCIAL_AUTH_GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS = {'hd': 'iitj.ac.in'}

SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['username', 'email']

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('GOOGLE_OAUTH2_KEY', default='', cast=str)

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('GOOGLE_OAUTH2_SECRET', default='', cast=str)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
)

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'last_name', 'email']

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True

HITCOUNT_KEEP_HIT_ACTIVE = {'minutes': 1}

# CKEditor
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Basic',
        'width': '100%',
        'tabSpaces': 4,
        'mathJaxLib': 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_HTML',
        'toolbar_Basic': [
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            # {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'formulae', 'items': ['Mathjax']},
            {'name': 'insert',
             'items': ['Image', 'Table', 'HorizontalRule', 'Smiley', ]},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', ]},
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
        ],
        'extraPlugins': ','.join([
            'uploadimage',
            'div',
            'autolink',
            'iframe',
            'embed',
            'embedsemantic',
            'autoembed',
            'autogrow',
            'uploadimage',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'mathjax',
            'codesnippet',
        ]),
    },
}

VERSATILEIMAGEFIELD_SETTINGS = {
    # The amount of time, in seconds, that references to created images
    # should be stored in the cache. Defaults to `2592000` (30 days)
    'cache_length': 36000,
    # The name of the cache you'd like `django-versatileimagefield` to use.
    # Defaults to 'versatileimagefield_cache'. If no cache exists with the name
    # provided, the 'default' cache will be used instead.
    'cache_name': 'versatileimagefield_cache',
    # The save quality of modified JPEG images. More info here:
    # https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#jpeg
    # Defaults to 70
    'jpeg_resize_quality': 85,
    # The name of the top-level folder within storage classes to save all
    # sized images. Defaults to '__sized__'
    'sized_directory_name': 'resized',
    # The name of the directory to save all filtered images within.
    # Defaults to '__filtered__':
    'filtered_directory_name': 'filtered',
    # The name of the directory to save placeholder images within.
    # Defaults to '__placeholder__':
    'placeholder_directory_name': 'placeholder',
    # Whether or not to create new images on-the-fly. Set this to `False` for
    # speedy performance but don't forget to 'pre-warm' to ensure they're
    # created and available at the appropriate URL.
    'create_images_on_demand': True,
    # A dot-notated python path string to a function that processes sized
    # image keys. Typically used to md5-ify the 'image key' portion of the
    # filename, giving each a uniform length.
    # `django-versatileimagefield` ships with two post processors:
    # 1. 'versatileimagefield.processors.md5' Returns a full length (32 char)
    #    md5 hash of `image_key`.
    # 2. 'versatileimagefield.processors.md5_16' Returns the first 16 chars
    #    of the 32 character md5 hash of `image_key`.
    # By default, image_keys are unprocessed. To write your own processor,
    # just define a function (that can be imported from your project's
    # python path) that takes a single argument, `image_key` and returns
    # a string.
    'image_key_post_processor': None,
    # Whether to create progressive JPEGs. Read more about progressive JPEGs
    # here: https://optimus.io/support/progressive-jpeg/
    'progressive_jpeg': False
}

VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    'festival': [
        ('full_size', 'url'),
        ('thumbnail', 'thumbnail__100x100'),
        ('medium_square_crop', 'crop__400x400'),
        ('small_square_crop', 'crop__50x50')
    ],
    'image': [
        ('full_size', 'url')
    ]
}

HOME_PAGE_CAROUSEL_GALLERY_SLUG = config('HOME_PAGE_CAROUSEL_GALLERY_SLUG', cast=str, default='home-carousel')
HOME_PAGE_GALLERY_SLUG = config('HOME_PAGE_GALLERY_SLUG', cast=str, default='home-gallery')

CORS_ORIGIN_ALLOW_ALL = DEBUG

GRAPHENE = {
    'SCHEMA': 'gymkhana.schema.schema',
    'SCHEMA_INDENT': 2,
    'RELAY_CONNECTION_MAX_LIMIT': 100,
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}

if not DEBUG:
    REST_FRAMEWORK = {
        # Use Django's standard `django.contrib.auth` permissions.
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        ),
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
        ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.SessionAuthentication',
        )
    }

PHOTOLOGUE_DIR = 'gallery'

SERVER_EMAIL = 'noreply@localhost.com'
DEFAULT_FROM_EMAIL = 'noreply@localhost.com'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' if DEBUG else \
    'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='noreply@localhost.com', cast=str)
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='', cast=str)

GRAPHQL_JWT = {
    'JWT_AUTH_HEADER_PREFIX': 'Bearer'
}
