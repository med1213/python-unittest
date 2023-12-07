from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
import json
from django.test.client import encode_multipart, RequestFactory
from ..models import Footer
from django.contrib.auth.models import User


class FooterTestCase(APITestCase):

    def setUp(self) -> None:

        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
        
        self.footer = Footer.objects.create(id=2,
                                            address="donkoi",
                                            email="donkoi@gmail.com",
                                            instagram_url='https://www.facebook.com/BesTech.la/',
                                            facebook_url='https://www.facebook.com/BesTech.la/',
                                            whatsapp='020965641',
                                            is_active=True,)

        
        self.data = {
            "address": "add",
            "email": "test@gmail.com",
            "instagram_url": "https://www.facebook.com/BesTech.la/",
            "facebook_url": "https://www.facebook.com/BesTech.la/",
            "whatsapp": "5555",
            "is_active": "true"
        }

        self.urls = reverse('footer_list')
        self.url = reverse(('footer_detail'), kwargs={'pk': 2})

    def test_get_all_footers(self):
        response = self.client.get(self.urls)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_new_footer(self):

        response = self.client.post(self.urls, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_footer(self):

        response = self.client.patch(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_footer(self):

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class FilterFooterAPITestCase(APITestCase):

    def setUp(self) -> None:

        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
        self.footer = Footer.objects.create(id=1,
                                            address="donkoi",
                                            email="donkoi@gmail.com",
                                            instagram_url='https://www.facebook.com/BesTech.la/',
                                            facebook_url='https://www.facebook.com/BesTech.la/',
                                            whatsapp='020965641',
                                            is_active=True,)
        
        self.url = '{url}?{filter}={value}'.format(
            url=reverse('footer_list'),
            filter='is_active', value='true')
        
    def test_filter_footer_by_status(self):

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)