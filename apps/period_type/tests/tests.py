from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from apps.period_type.models import PeriodType
from django.contrib.auth.models import User


class CreateTestPeriodType(APITestCase):

    def setUp(self):
        self.period_urls = reverse('period_types')
        self.period_url = reverse('period_type', kwargs={'pk': 2})

        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
        
        self.period_data = PeriodType.objects.create(id=2, period_type='big', is_active=True)
        
        self.data = {
            "period_type": 'small',
            "is_active": True
        }


    def test_get_all(self):

        response = self.client.get(self.period_urls,)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['count'], int)
        self.assertEqual(response.data['count'],1)

    def test_get_one(self):
        response = self.client.get(self.period_url,)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.period_data.period_type, "big")

    def test_create(self):

        response = self.client.post(self.period_urls, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['period_type'], self.data['period_type'])

    def test_update(self):

        response = self.client.patch(self.period_url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['period_type'], self.data['period_type'])

    def test_delete(self):

        response = self.client.delete(self.period_url, )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class FilterUsercandidateAPITestCase(APITestCase):
    def setUp(self) -> None:

        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')

        self.period_data = PeriodType.objects.create(id=1, period_type='big', is_active=True)

        self.urls = '{url}?{filter}={value}&{filter1}={value1}&{filter2}={value2}'.format(
            url=reverse('period_types'),
            filter='', value='', filter1='is_active', value1= 'true', filter2='', value2='')
        
        return super().setUp()
    
    def test_filter_candidate(self):
        res = self.client.get(self.urls)
        self.assertEqual(res.status_code, status.HTTP_200_OK)