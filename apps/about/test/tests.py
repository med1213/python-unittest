from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
import io
from PIL import Image
from ..models import About

from django.contrib.auth.models import User

# Create your tests here.
class TestCaseAbout(APITestCase):

    urls = reverse('abouts')
    url = reverse(('about'), kwargs={'pk':1})

    def test_create_about(self):


        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
        
        photo_file = self.generate_photo_file()
        data = {
            'title': 'test title',
            'description': 'test content',
            "image": photo_file,
            'is_active': "true"
        }
        response = self.client.post(self.urls, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def test_get_about(self):

        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
        
        response = self.client.get(self.urls)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_about_by_id(self):
        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
        self.about = About.objects.create(id=1,title= 'test title',
                                            description= 'test content',
                                            image= "http://127.0.0.1:8000/media/Title1_PAD36F9.png",
                                            is_active=True)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_about(self):
        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
        self.about = About.objects.create(id=1,title= 'test title',
                                            description= 'test content',
                                            image= "http://127.0.0.1:8000/media/Title1_PAD36F9.png",
                                            is_active=True)
        
        photo_file = self.generate_photo_file()
        data = {
            'title': 'test title',
            'description': 'test content',
            "image": photo_file,
            'is_active': "true"
        }
        response = self.client.put(self.url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_about(self):
        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
        self.about = About.objects.create(  id=1,title= 'test title',
                                            description= 'test content',
                                            image= "http://127.0.0.1:8000/media/Title1_PAD36F9.png",
                                            is_active=True)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class FilterAboutTestCase(APITestCase):

    def test_filter_village_by_status(self):

        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')

        self.about = About.objects.create(id=1,title= 'test title',
                                            description= 'test content',
                                            image= "http://127.0.0.1:8000/media/Title1_PAD36F9.png",
                                            is_active=True)

        url = '{url}?{filter}={value}'.format(
            url=reverse('abouts'),
            filter='is_active', value='true')
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
