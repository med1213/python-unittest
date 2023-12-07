import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'lucky_draw_core.settings_prod')

application = get_wsgi_application()
