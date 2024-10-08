"""
WSGI config for savannah project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'savannah.settings')

application = get_wsgi_application()

# app = application # this is to allow the application to be accessed from the main project folder