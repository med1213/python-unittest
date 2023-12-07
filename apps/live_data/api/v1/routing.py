from django.urls import re_path, path

from . import consumers


websocket_urlpatterns = [
    re_path(r"^ws/$", consumers.LiveDataConsumer.as_asgi()),
    path('ws/spin/', consumers.RealTimeSpinerConsumer.as_asgi(), name="real-time"),
]