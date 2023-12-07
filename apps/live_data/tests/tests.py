# from channels.testing import WebsocketCommunicator
# from django.test import TestCase
# from django.urls import reverse
# from rest_framework.test import APIClient
# from live_data.api.v1.consumers import RealTimeSpinerConsumer

# class LiveDataConsumerTestCase(TestCase):

#     async def test_send_message(self):
#         communicator = WebsocketCommunicator(RealTimeSpinerConsumer.as_asgi(), "/ws/spin/")
#         connected, _ = await communicator.connect()
#         self.assertTrue(connected)

#         message = {'type': 'message', 'text': 'Hello, world!'}
#         await communicator.send_json_to(message)

#         response = await communicator.receive_json_from()
#         self.assertEqual(response, {'type': 'message', 'text': 'Hello, world!'})

#         await communicator.disconnect()
