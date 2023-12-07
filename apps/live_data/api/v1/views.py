from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from apps.winner.models import Winner
from .serializers import LiveDataSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class LiveDataViewSet(viewsets.ModelViewSet):

    serializer_class = LiveDataSerializer
    queryset = Winner.objects.all()


def index(request):
    return render(request, "demo/index.html")

def my_view(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "mygroup",
        {
            "type": "myevent",
            "message": "Hello, world!",
        },
    )
    return HttpResponse("Event sent")