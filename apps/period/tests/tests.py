from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from apps.prize_type.models import PrizeType
from apps.period_type.models import PeriodType
from apps.period.models import Period
from datetime import datetime
from django.contrib.auth.models import User


class TestPeriod(APITestCase):

    def setUp(self):
        self.period_urls = reverse('periods')
        self.period_url = reverse('period', kwargs={'pk': 2})

        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')

        self.period_type_data = PeriodType.objects.create(
            id=1, period_type='big', is_active=True)
        self.prize_type_data = PrizeType.objects.create(
            id=1, prize_type='big', is_active=True)
        self.period_data = Period.objects.create(id=2,
                                                 period="1",
                                                 #  prize_type=[1],
                                                 #  period_type=[1],
                                                 open_date="2023-04-06",
                                                 close_date="2023-04-06",
                                                 is_active=True)

        self.data = {
            "period": '1',
            "prize_type": [1],
            "period_type": [1],
            "open_date": datetime.now(),
            "close_date": datetime.now(),
            "is_active": True
        }

    def test_get_all(self):

        response = self.client.get(self.period_urls,)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['count'], int)
        self.assertEqual(response.data['count'], 1)

    def test_create(self):

        response = self.client.post(self.period_urls, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update(self):

        response = self.client.patch(self.period_url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['prize_type'], self.data['prize_type'])

    def test_delete(self):

        response = self.client.delete(self.period_url, )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class FilterPeriodAPITestCase(APITestCase):
    def setUp(self) -> None:

        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')

        self.period_type_data = PeriodType.objects.create(
            id=1, period_type='big', is_active=True)
        self.prize_type_data = PrizeType.objects.create(
            id=1, prize_type='big', is_active=True)
        self.period_data = Period.objects.create(id=2,
                                                 period="1",
                                                 open_date="2023-04-06",
                                                 close_date="2023-04-06",
                                                 is_active=True)

        self.urls = '{url}?{filter}={value}&{filter1}={value1}&{filter2}={value2}'.format(
            url=reverse('periods'),
            filter='depth', value='true', filter1='is_active', value1='true', filter2='', value2='')

        return super().setUp()

    def test_filter_period(self):
        res = self.client.get(self.urls)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
