"""
It exposes the WSGI callable as a module-level variable named ``application``.
"""
import os
import json
from django.core.wsgi import get_wsgi_application

DIR_PATH_FILE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(DIR_PATH_FILE, '.config_project/conf.json')) as json_file:
    confs = json.loads(json_file.read())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', confs['generals']['settings'])

application = get_wsgi_application()
