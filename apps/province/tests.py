from django.test import TestCase
from django.urls import path, reverse, include, resolve
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework import status
import json
from .api.v1.views import ListCreateAPIView
from .models import Province
from django.contrib.auth.models import User


class ProvinceTestCase(APITestCase):

    def setUp(self):
        self.url = reverse("province_list")

        self.province_data = {"province": "pakse", "is_active": True}
        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')

    def test_create(self):
        response = self.client.post(self.url, self.province_data, format="json")
        self.assertEqual(response.data['province'], self.province_data['province'])
        self.assertEqual(response.data['is_active'], self.province_data['is_active'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_province(self):
         
        self.province = Province.objects.create(id = 5, province = "pakse", is_active=True)  
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['count'], int)
        self.assertEqual(response.data['count'],1)
        self.assertEqual(self.province.province, "pakse")

class ListProviderTestCase(APITestCase):    

    def setUp(self):    
        self.url = reverse(('provinces'), kwargs={'pk': 5})  
        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
        self.province = Province.objects.create(id = 5, province = "pakse", is_active=True)        
        self.data = {"province": "pakse1111", "is_active": False}

    def test_update(self):
        response = self.client.patch(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['province'], self.data['province'])
        self.assertEqual(response.data['is_active'], self.data['is_active'])

    def test_get_one_province(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.province.province, "pakse")
        self.assertEqual(self.province.is_active, True)

    def test_delete(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class FilterProvinceTestCase(APITestCase):

    def setUp(self) -> None:
        self.province = Province.objects.create(id=1, province="vientaince", is_active=True)

        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
        
        self.url_active = '{url}?{filter}={value}'.format(
            url=reverse('province_list'),
            filter='is_active', value='false')
        
        self.url_province = '{url}?{filter}={value}'.format(
            url=reverse('province_list'),
            filter='province', value='champasak')

    def test_filter_province_by_is_active(self):
        
        response = self.client.get(self.url_active)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.province.is_active, True)

    def test_filter_province_by_name(self):
        
        
        response = self.client.get(self.url_province)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.province.province, "vientaince")
