"""

Django | Base project | 22 Ago 2020

Generated by 'django-admin startproject' using Django 2.2.2

"""
import os
import re
import json
import environ
from BaseProject.core.settings import Settings
from django.utils.translation import gettext_lazy as _


class BaseSettings(Settings):
    """ Community base settings, don't use this directly. """
    # Main Path
    SITE_ROOT = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    env = environ.Env(
        DEBUG=(bool, False),
        DISABLE_EXISTING_LOGGERS=(bool, False),
        SECRET_KEY=str,
        INTERNAL_IPS=(list, ['127.0.0.1']),
        ALLOWED_HOSTS=(list, ['127.0.0.1']),
        ADMINS=str,
        DB_ENGINE=str,
        DATABASE_URL=str,
        REDIS_SERVER=str,
        CACHE_PREFIX=str,
        CACHE_TIMEOUT=int,
        EMAIL_URL=str,
        DEFAULT_FROM_EMAIL=str,
        SENTRY_DSN=str,
        ENABLE_REMOTE_STORAGE=(bool, False),
        BUCKET_NAME=str,
        AWS_ACCESS_KEY_ID=str,
        AWS_SECRET_ACCESS_KEY=str,
        AWS_STORAGE_BUCKET_NAME=str,
        CELERY_BROKER_URL=str,
        CELERY_TIMEZONE=str,
        ADMIN_SITE_HEADER=str,
        ADMIN_SITE_TITLE=str,
        ADMIN_SITE_INDEX_TITLE=str,
        PROJECT=str,
        LOGIN_REDIRECT_URL=str,
        LOG_CONSOLE_LEVEL=str,
        LOG_FILE_DJANGO_LEVEL=str,
    )
    env_path = None
    if os.environ['DJANGO_SETTINGS_MODULE'] == 'BaseProject.settings.dev':
        env_path = os.path.join(SITE_ROOT, '.config_project/environ/dev/.env')
    elif os.environ['DJANGO_SETTINGS_MODULE'] == 'BaseProject.settings.production':
        env_path = os.path.join(SITE_ROOT, '.config_project/environ/production/.env')

    environ.Env.read_env(env_path)  # reading .env file

    SECRET_KEY = env('SECRET_KEY')

    AUTH_USER_MODEL = 'custom_user.User'

    SITE_ID = 1
    ROOT_URLCONF = 'BaseProject.core.urls'
    # LOGIN_REDIRECT_URL = '/dashboard/'  < posible uso ! >

    # Debug settings
    DEBUG = env('DEBUG')

    WSGI_APPLICATION = 'BaseProject.core.wsgi.application'

    DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
    EMAIL_URL = env.email()  # == EMAIL_URL = env.email_url('EMAIL_URL')
    EMAIL_BACKEND = EMAIL_URL['EMAIL_BACKEND']
    EMAIL_HOST = EMAIL_URL['EMAIL_HOST']
    EMAIL_HOST_PASSWORD = EMAIL_URL['EMAIL_HOST_PASSWORD']
    EMAIL_HOST_USER = EMAIL_URL['EMAIL_HOST_USER']
    EMAIL_PORT = EMAIL_URL['EMAIL_PORT']
    EMAIL_USE_TLS = EMAIL_URL['EMAIL_USE_TLS']

    @property
    def ADMINS(self):  # noqa
        admins_emails = self.env('ADMINS')
        return list(email for email in json.loads(admins_emails))

    MANAGERS = ADMINS  # Broken Links

    # Application Classes
    @property
    def INSTALLED_APPS(self):  # noqa
        apps = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',

            'django.contrib.humanize',
            'django.contrib.sites',

            # Third party apps
            'stdimage',
            'rest_framework',
            'rest_framework.authtoken',
            'corsheaders',
            'django_filters',
            'widget_tweaks',

            'allauth',
            'allauth.account',
            'allauth.socialaccount',
            'django_celery_beat',

            'phonenumber_field',

            # Project apps
            'BaseProject.apps.custom_user',
            'BaseProject.apps.admin_theme',
        ]
        return apps

    # Admin Vars
    ADMIN_SITE_HEADER = env('ADMIN_SITE_HEADER')
    ADMIN_SITE_TITLE = env('ADMIN_SITE_TITLE')
    ADMIN_SITE_INDEX_TITLE = env('ADMIN_SITE_INDEX_TITLE')
    PROJECT = env('PROJECT')
    SITE_URL = '/'  # ToDo => Cambiar por reverse resolution url

    @property
    def DATABASES(self):  # noqa
        db_engine = self.env('DB_ENGINE')
        if db_engine == 'postgres':
            return {
                'default': self.env.db()
            }
        return {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(self.SITE_ROOT, 'dev.db'),
            }
        }

    FIXTURE_DIRS = [os.path.join(SITE_ROOT, '.config_project/DB_Fixtures')]  # No debe cambiar el path de este dir

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',  # Es un default!
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.common.BrokenLinkEmailsMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'corsheaders.middleware.CorsMiddleware',
    ]

    AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")

    # Assets and Media
    if env('ENABLE_REMOTE_STORAGE'):
        AWS_STATIC_LOCATION = 'static'
        AWS_MEDIA_LOCATION = 'media'
        AWS_S3_OBJECT_PARAMETERS = {
            'CacheControl': 'max-age=86400',
        }
        bucket_name = env('BUCKET_NAME')
        AWS_STORAGE_BUCKET_NAME = F'{bucket_name}-bucket-service'
        AWS_S3_CUSTOM_DOMAIN = '{0}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)

        STATICFILES_STORAGE = 'BaseProject.core.custom_storages.CustomStaticStorage'
        DEFAULT_FILE_STORAGE = 'BaseProject.core.custom_storages.CustomMediaStorage'
        STATIC_URL = 'https://{0}/{1}/'.format(AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)
    else:
        STATIC_URL = '/static/'
        STATIC_ROOT = os.path.join(SITE_ROOT, '.static')

        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(SITE_ROOT, '.media')

    STATICFILES_DIRS = [
        os.path.join(SITE_ROOT, 'BaseProject/static'),
    ]

    STATICFILES_FINDERS = [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    ]

    TEMPLATE_ROOT = os.path.join(SITE_ROOT, 'BaseProject/templates')

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [TEMPLATE_ROOT],
            'OPTIONS': {
                'debug': DEBUG,
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
                'loaders': [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ],
            },
        },
    ]

    SITE_ID = 1

    AUTHENTICATION_BACKENDS = [
        'django.contrib.auth.backends.ModelBackend',
        'allauth.account.auth_backends.AuthenticationBackend',
    ]

    @property
    def LOGIN_REDIRECT_URL(self):
        login_redirect_url = self.env("LOGIN_REDIRECT_URL")
        return login_redirect_url

    LOGIN_URL = 'account_login'
    ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        ),
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        ]
    }

    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            'PREFIX': env('CACHE_PREFIX'),
            'TIMEOUT': env('CACHE_TIMEOUT'),
            "LOCATION": env('REDIS_SERVER'),
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        }
    }
    # CACHE_MIDDLEWARE_SECONDS = 60  # seconds per page, default 600

    # I18n
    TIME_ZONE = 'America/Cancun'
    USE_TZ = True
    LANGUAGE_CODE = 'es-mx'
    USE_I18N = True
    USE_L10N = True
    LOCALE_PATHS = [
        os.path.join(SITE_ROOT, 'BaseProject/locale'),
    ]
    LANGUAGES = [
        ('en-us', _('Inglés')),
        ('es-mx', _('Español')),
    ]

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
            'OPTIONS': {
                'min_length': 9,
            }
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    # Security & X-Frame-Options Middleware
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'

    # CORS
    CORS_ALLOW_HEADERS = (
        'x-requested-with',
        'content-type',
        'accept',
        'origin',
        'authorization',
        'x-csrftoken'
    )

    ALLOWED_HOSTS = env('ALLOWED_HOSTS')

    INTERNAL_IPS = env('INTERNAL_IPS')

    # Logging
    @property
    def SENTRY(self):
        if not self.DEBUG:
            import sentry_sdk
            from sentry_sdk.integrations.django import DjangoIntegration
            return sentry_sdk.init(
                dsn=self.env('SENTRY_DSN'),
                integrations=[DjangoIntegration()]
            )

    IGNORABLE_404_URLS = [
        re.compile(r'\.(php|cgi)$'),
        re.compile(r'^/phpmyadmin/'),
        re.compile(r'^/apple-touch-icon.*\.png$'),
        re.compile(r'^/favicon\.ico$'),
        re.compile(r'^/robots\.txt$'),
    ]

    LOGS_ROOT = os.path.join(SITE_ROOT, '.logs')
    LOG_FORMAT = '|| %(levelname)s || %(asctime)s || %(module)s || %(name)s || %(lineno)s[%(process)d] || %(message)s'
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': LOG_FORMAT,
                'datefmt': '%d/%b/%Y %H:%M:%S',
            },
        },
        'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            },
        },
        'handlers': {
            'console': {
                'level': env('LOG_CONSOLE_LEVEL'),
                'class': 'logging.StreamHandler',
                'formatter': 'default'
            },
            'debug': {
                'level': env('LOG_FILE_DJANGO_LEVEL'),
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOGS_ROOT, 'django/debug.log'),
                'formatter': 'default',
            },
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'formatter': 'default',
                'class': 'django.utils.log.AdminEmailHandler',
                'include_html': True,
            },
            'null': {
                'class': 'logging.NullHandler',
            },
        },
        'loggers': {
            '': {
                'handlers': ['debug', 'console', 'mail_admins'],
                'level': 'DEBUG',
            },
            'django': {
                'handlers': ['debug', 'console', 'mail_admins'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'BaseProject': {
                'handlers': ['debug', 'console', 'mail_admins'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'django.security.DisallowedHost': {
                'handlers': ['null'],
                'propagate': False,
            },
        },
    }
