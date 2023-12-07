"""
ASGI config for bbi_ecomm project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter

from apps.live_data.api.v1.routing import websocket_urlpatterns


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'lucky_draw_core.settings_prod')

application = get_asgi_application()


application = ProtocolTypeRouter({
    "http": application,
    "websocket": URLRouter(websocket_urlpatterns),
})