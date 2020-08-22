import os
import sys
import json

DIR_PATH_FILE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(DIR_PATH_FILE, '../../.config_project/conf.json')) as json_file:
    confs = json.loads(json_file.read())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', confs['generals']['settings'])

from django.core.management import execute_from_command_line  # noqa: E402
execute_from_command_line(sys.argv)
