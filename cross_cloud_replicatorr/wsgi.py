# cross_cloud_replicator/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cross_cloud_replicatorr.settings')
application = get_wsgi_application()
