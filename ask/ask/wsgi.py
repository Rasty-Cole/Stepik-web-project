"""
WSGI config for ask project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append("/mnt/d/Programs-PartII/Dropbox/Stepik.org/Web-technology/web-project-stepik/stepik/lib/python3.5/site-packages")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ask.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
