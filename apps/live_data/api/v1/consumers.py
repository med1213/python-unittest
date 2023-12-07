import json
from djangochannelsrestframework import permissions
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin
from djangochannelsrestframework.observer import model_observer
from channels.consumer import AsyncConsumer
import json
from channels.generic.websocket import AsyncWebsocketConsumer

from apps.winner.models import Winner
from .serializers import LiveDataSerializer

class LiveDataConsumer(ListModelMixin, GenericAsyncAPIConsumer):

    queryset = Winner.objects.all()
    serializer_class = LiveDataSerializer
    permissions = (permissions.AllowAny,) 

    async def connect(self, **kwargs):
        await self.model_change.subscribe()
        await super().connect()

    @model_observer(Winner)
    async def model_change(self, message, observer=None, **kwargs):
        await self.send_json(message)

    @model_change.serializer
    def model_serialize(self, instance, action, **kwargs):
        return dict(data=LiveDataSerializer(instance=instance).data, action=action.value)


class RealTimeSpinerConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        group = "mygroup"
        self.group = group
        await self.channel_layer.group_add(group, self.channel_name)
        await self.send({
            "type": "websocket.accept",
        })
        print("WebSocket client connected")

    async def websocket_receive(self, event):
        intial_data = event.get("text", None)
        await self.channel_layer.group_send(
            self.group, {
            'type': "group_message",
            'text': intial_data
            }
        )
        print('get msg from ...', intial_data)

    async def group_message(self, event):
        print('get group msg from client ...', event)
        await self.send({
            "type": "websocket.send",
            "text": event['text']
        })

    async def websocket_disconnect(self, event):
        print("WebSocket client disconnected", event)