from apps.lucky_draw.api.v1.serializers import LuckyDrawSerializer
from apps.lucky_draw.models import LuckyDraw
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from datetime import datetime, timedelta
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from apps.lucky_draw.models import LuckyDraw
from django.contrib.auth.models import User


# class LuckyDrawTests(TestCase):
#     def setUp(self):

#         self.testuser1 = User.objects.create_superuser(
#             username='admin', password='admin')

#         self.client.login(username=self.testuser1.username,
#                           password='admin')
#         self.client = APIClient()
#         self.ld1 = LuckyDraw.objects.create(
#             item_name='Test Item 1', is_active=True)
#         self.ld2 = LuckyDraw.objects.create(
#             item_name='Test Item 2', is_active=True)
#         self.ld3 = LuckyDraw.objects.create(
#             item_name='Test Item 3', is_active=False)
#         self.ld4 = LuckyDraw.objects.create(
#             item_name='Test Item 4', is_active=True, updated_on=datetime.now() - timedelta(days=1))
        
#         self.url = reverse('lucky_draws')
        
#         self.random_url = reverse('lucky_draw_random')

#     def tearDown(self):
#         LuckyDraw.objects.all().delete()

#     def test_create_lucky_draw(self):
#         data = {'item_name': 'Test Item 4'}
#         response = self.client.post(self.url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(LuckyDraw.objects.count(), 5)
#         self.assertEqual(response.data['item_name'], 'Test Item 4')
#         self.assertEqual(response.data['is_active'], True)
#         self.assertTrue('id' in response.data)
#         response_data = response.json()
#         print(response_data)

#     def test_get_lucky_draws(self):
#         response = self.client.get(self.url, format='json')
#         self.assertEqual(response.status_code, 200)


#     def test_get_lucky_draws(self):
#         response = self.client.get(self.random_url, format='json')
#         json_data = response.json()
#         self.assertEqual(response.status_code, 200)

class FilterLuckyDrawAPITestCase(APITestCase):
    def setUp(self) -> None:

        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')

        self.lucky_draw1 = LuckyDraw.objects.create(id=2,
                                                 item_name="new draw",
                                                 is_active=True
                                                )
        self.lucky_draw = LuckyDraw.objects.create(id=3,
                                                 item_name="new draw",
                                                 is_active=False
                                                )

        self.urls = '{url}?{filter}={value}&{filter1}={value1}&{filter2}={value2}'.format(
            url=reverse('lucky_draws'),
            filter='depth', value='true', filter1='is_active', value1='true', filter2='', value2='')
        
        self.urls_random = '{url}?{filter}={value}'.format(
            url=reverse('lucky_draw_random'),
            filter='is_active', value='false',)

        return super().setUp()

    def test_filter_luckyDraw(self):
        res = self.client.get(self.urls)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIsInstance(res.data['count'], int)
        self.assertEqual(res.data['count'], 1)
        self.assertEqual(self.lucky_draw1.item_name, "new draw")
        self.assertEqual(self.lucky_draw1.is_active, True)

    def test_filter_luckyDraw_random(self):
        res = self.client.get(self.urls_random)
        json_data = res.json()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
