import os
import json
# import django
import environ
from django.conf import settings
import logging
from celery import Celery


SITE_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    with open(os.path.join(SITE_ROOT, '.config_project/conf.json')) as json_file:
        confs = json.loads(json_file.read())

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', confs['generals']['settings'])

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
)
env_path = None
if os.environ['DJANGO_SETTINGS_MODULE'] == 'BaseProject.settings.dev':
    env_path = os.path.join(SITE_ROOT, '.config_project/environ/dev/.env')
elif os.environ['DJANGO_SETTINGS_MODULE'] == 'BaseProject.settings.production':
    env_path = os.path.join(SITE_ROOT, '.config_project/environ/production/.env')

environ.Env.read_env(env_path)  # reading .env file

logger = logging.getLogger(__name__)

app = Celery('BackgroundTasksApp1')

app.config_from_object('django.conf:settings', namespace='CELERY')

# django.setup()

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
