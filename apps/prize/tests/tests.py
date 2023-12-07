from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from apps.prize_type.models import PrizeType
from apps.prize.models import Prize
from django.contrib.auth.models import User


class CreateTestPrizeType(APITestCase):

    def setUp(self):
        self.prize_urls = reverse('prizes')
        self.prize_url = reverse('prize', kwargs={'pk': 2})
        self.prize_data = PrizeType.objects.create(id=1, prize_type='big', is_active=True)
        self.prize_data = Prize.objects.create(id=2, prize='moto', detail='moto', quantity='1', is_active=True, prize_type_id=1)
        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
        
        self.data = {
            "prize_type": 1,
            "prize": 'small',
            "detail": 'small',
            "quantity": '2',
            "is_active": True
        }


    def test_get_all(self):

        response = self.client.get(self.prize_urls,)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['count'], int)
        self.assertEqual(response.data['count'],1)

    def test_get_one(self):
        response = self.client.get(self.prize_url,)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.prize_data.prize, "moto")

    def test_create(self):

        response = self.client.post(self.prize_urls, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['prize'], self.data['prize'])

    def test_update(self):

        response = self.client.patch(self.prize_url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['prize'], self.data['prize'])

    def test_delete(self):

        response = self.client.delete(self.prize_url, )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class FilterAPITestCase(APITestCase):
    def setUp(self) -> None:        
        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
        self.prize_data = PrizeType.objects.create(id=1, prize_type='big', is_active=True)
        self.prize_data = Prize.objects.create(id=2, prize='moto', detail='moto', quantity='1', is_active=True, prize_type_id=1)

        self.urls = '{url}?{filter}={value}&{filter1}={value1}&{filter2}={value2}'.format(
            url=reverse('prizes'),
            filter='depth', value='true', filter1='is_active', value1= 'true', filter2='', value2='')
        
        return super().setUp()
    
    def test_filter_prize(self):
        res = self.client.get(self.urls)
        self.assertEqual(res.status_code, status.HTTP_200_OK)