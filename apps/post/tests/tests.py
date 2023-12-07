from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from apps.period.models import Period
from apps.post.models import Post
import io
from PIL import Image
from django.contrib.auth.models import User

class PostTestCase(APITestCase):

    urls = reverse("posts")
    url = reverse(('post'), kwargs={'pk': 1})

    
    def test_view_posts(self):
        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
        response = self.client.get(self.urls, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_post(self):
        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
        self.test_post_period = Period.objects.create(id = 1, period='Period')
        self.test_post = Post.objects.create(id=1, 
                                             period_id = 1, 
                                             title= "test1", 
                                             sub_title = "test sub", 
                                             description = "test description", 
                                             phone = "test pone", 
                                             address = "test address", 
                                             image = "test image", 
                                             is_active = True)
        
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
        self.test_post = Period.objects.create(id= 1, period='Period')
        photo_file = self.generate_photo_file()

        data = {
            "period" : 1, 
            "title": "xaythany", 
            "sub_title": "xaythany", 
            "description": "xaythany", 
            "phone": "xaythany", 
            "address": "xaythany", 
            "image": photo_file, 
            "is_active": "true"
            }

        response = self.client.post(self.urls, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update(self):
        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
        self.test_post_period = Period.objects.create(id = 1, period='Period')
        self.test_post = Post.objects.create(id=1, 
                                             period_id = 1, 
                                             title= "test1", 
                                             sub_title = "test sub", 
                                             description = "test description", 
                                             phone = "test pone", 
                                             address = "test address", 
                                             image = "test image", 
                                             is_active = True)
        
        photo_file = self.generate_photo_file()

        data = {
            "period" : 1, 
            "title": "xaythany1", 
            "sub_title": "xaythany1", 
            "description": "xaythany1", 
            "phone": "xaythany1", 
            "address": "xaythany1", 
            "image": photo_file, 
            "is_active": "true"
            }

        response = self.client.put(self.url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
        self.test_post_period = Period.objects.create(id = 1, period='Period')
        self.test_post = Post.objects.create(id=1, 
                                             period_id = 1, 
                                             title= "test1", 
                                             sub_title = "test sub", 
                                             description = "test description", 
                                             phone = "test pone", 
                                             address = "test address", 
                                             image = "test image", 
                                             is_active = True)
        
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file
    
class FilterPostAPITestCase(APITestCase):

    def setUp(self) -> None:

        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
        self.test_post_period = Period.objects.create(id = 1, period='Period')
        self.test_post = Post.objects.create(id=1, 
                                             period_id = 1, 
                                             title= "test1", 
                                             sub_title = "test sub", 
                                             description = "test description", 
                                             phone = "test pone", 
                                             address = "address", 
                                             image = "media/test_6sV3lMu.png", 
                                             is_active = True)
        
        self.url = '{url}?{filter}={value}'.format(
            url=reverse('posts'),
            filter='period', value='1')
        self.post_url = '{url}?{filter}={value}'.format(
            url=reverse('posts'),
            filter='title', value='test')
        self.urls = '{url}?{filter}={value}&{filter1}={value1}&{filter2}={value2}'.format(
            url=reverse('posts'),
            filter='depth', value='true', filter1='is_active', value1= 'true', filter2='', value2='')
    
    def test_filter_by_period_id(self):
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_by_post_title(self):
        
        response = self.client.get(self.post_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_by_post_status(self):

        response = self.client.get(self.urls)
        self.assertEqual(response.status_code, status.HTTP_200_OK)