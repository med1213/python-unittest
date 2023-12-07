from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
import io
from PIL import Image
from ..models import Slide
from django.contrib.auth.models import User

# Create your tests here.
class SlideTestCase(APITestCase):

    def setUp(self) -> None:    
        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')    
        self.slider = Slide.objects.create(id=2, title="sloider one", image= "", is_active=True)
        image_file = self.generate_photo_file()
        self.data={
            'title': 'test update slide', 
            'image': image_file, 
            'is_active': "true"
        }
        self.urls = reverse('slides')
        self.url = reverse(('slide'), kwargs={'pk': 2})

    def test_get_all_slides(self):
        response = self.client.get(self.urls)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_specific_slide(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_new_slide(self):
        response = self.client.post(self.urls, self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def test_update_slider(self):
        response = self.client.put(self.url, self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_slider(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class FilterSlideAPITestCase(APITestCase):

    def setUp(self) -> None:
        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
        self.slide = Slide.objects.create(id=2, title="slide one", image= "http://127.0.0.1:8000/media/Screenshot_from_2023-03-16_11-57-21_DiYbmjP.png", is_active=True)
        self.url_active = '{url}?{filter}={value}'.format(
            url=reverse('slides'),
            filter='is_active', value='true')

    def test_filter_district_by_is_active(self):
        
        response = self.client.get(self.url_active)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.slide.is_active, True)