import os
import sys

# Path to your project
path = '/home/HarshGUmarkar/test'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'

# Activate virtualenv
activate_this = '/home/HarshGUmarkar/.virtualenvs/venv313/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
