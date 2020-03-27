"""
WSGI config for OnlineShopProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineShopProject.settings')

application = get_wsgi_application()

# def application(environ, start_response):
#     """Simplest possible application object"""
#     status = '200 OK'
#     response_headers = [('Content-type', 'text/plain')]
#     start_response(status, response_headers)
#     return [b'Hello world!\n']