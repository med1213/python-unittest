from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from ..models import UserProfile
import io
from PIL import Image


class ProfileTestCase(APITestCase):
    def setUp(self) -> None:
        self.urls = reverse('profiles')
        self.urls_admin = reverse('admin-update-profile', kwargs={'pk': 1})
        self.url = reverse('profile', kwargs={'pk': 1})

        self.test_user = User.objects.create(id= 2, username='super-admin',)
        self.data = {"owner": 2, "first_name": "first_name", "last_name": "last_name", "gender": "gender", "profile_pic": "profile_pic.png", "phone_number": "phone_number", "is_active": "true"}

        self.testuser1 = User.objects.create_superuser(
            username='admin1', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
    def test_get_all_profile(self):
        
        self.user = User.objects.create_superuser(
            id=4, username="admin", password='admin', is_active=True
        )
        self.client.login(username=self.user.username,
                          password='admin')
        self.profile_data = UserProfile.objects.create(
            id=1, 
            owner_id=4, 
            first_name="med", 
            last_name='bestech', 
            gender='gender', 
            profile_pic='profile_pic', 
            phone_number='phone_number', 
            is_active=True
        )
        response = self.client.get(self.urls, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['count'], int)
        self.assertEqual(response.data['count'],1)
        self.assertEqual(self.profile_data.first_name, "med")

    def test_get_one_profile(self):
        self.user = User.objects.create_superuser(
            id=4, username="admin", password='admin', is_active=True
        )
        self.client.login(username=self.user.username,
                          password='admin')
        self.create_data = UserProfile.objects.create(
            id=1, 
            first_name="best", 
            last_name="tech", 
            gender="Male", 
            profile_pic="", 
            phone_number="02055555", 
            is_active=True, 
            owner_id=4)

        res = self.client.get(self.url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(self.create_data.first_name, "best")
        self.assertEqual(self.create_data.is_active, True)

    def test_create_profile(self):
        self.test_user_data = User.objects.create(id= 7, username='super-admin2',)
        photo_file = self.generate_photo_file()
        self.data = {
            "owner": 7, 
            "first_name": "first_name", 
            "last_name": "last_name", 
            "gender": ['Male'], 
            "profile_pic": photo_file, 
            "phone_number": "phone_number", 
            "is_active": True}

        res = self.client.post(self.urls, self.data, format='multipart')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data['first_name'], self.data['first_name'])
        self.assertEqual(res.data['is_active'], self.data['is_active'])

    def test_update_profile(self):

        photo_file = self.generate_photo_file()
        self.test_user_update = User.objects.create_superuser(id= 12, username='super-admin2', password='admin')
        self.client.login(username=self.test_user_update.username, password='admin')
        self.create_data = UserProfile.objects.create(
            id=1, 
            first_name="best", 
            last_name="tech", 
            gender="Male", 
            profile_pic= "http://127.0.0.1:8000/media/Title1_PAD36F9.png", 
            phone_number="02055555", 
            is_active=True, 
            owner_id=12)
        
        self.data = {
            "owner": 12, 
            "first_name": "update first_name", 
            "last_name": "update last_name", 
            "gender": ['Male'], 
            "profile_pic": photo_file, 
            "phone_number": "phone_number", 
            "is_active": True}

        res = self.client.patch(self.url, self.data, format='multipart')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['first_name'], self.data['first_name'])
        self.assertEqual(res.data['phone_number'], self.data['phone_number'])

    def test_update_profile_validate(self):

        photo_file = self.generate_photo_file()
        self.test_user_update = User.objects.create_superuser(id= 12, username='super-admin2', password='admin')
        self.client.login(username=self.test_user_update.username, password='admin')
        self.create_data = UserProfile.objects.create(
            id=1, 
            first_name="best", 
            last_name="tech", 
            gender="Male", 
            profile_pic= "http://127.0.0.1:8000/media/Title1_PAD36F9.png", 
            phone_number="02055555", 
            is_active=True, 
            owner_id=12)
        
        self.data = {
            "owner": 12, 
            "first_name": "update first_name", 
            "last_name": "update last_name", 
            "gender": ['Male'], 
            "profile_pic": photo_file, 
            "phone_number": "phone_number", 
            "is_active": True}

        res = self.client.patch(self.urls_admin, self.data, format='multipart')
        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_delete_profile(self):

        self.test_user_update = User.objects.create_superuser(id= 12, username='super-admin2', password='admin')
        self.client.login(username=self.test_user_update.username, password='admin')
        self.create_data = UserProfile.objects.create(
            id=1, 
            first_name="best", 
            last_name="tech", 
            gender="Male", 
            profile_pic= "http://127.0.0.1:8000/media/Title1_PAD36F9.png", 
            phone_number="02055555", 
            is_active=True, 
            owner_id=12)
        res = self.client.delete(self.url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file
    
class FilterUserProfileAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.test_user = User.objects.create_superuser(id= 12, username='jonh', password='admin')
        self.client.login(username=self.test_user.username, password='admin')
        self.create_data = UserProfile.objects.create(
            id=1, 
            first_name="best", 
            last_name="tech", 
            gender="Male", 
            profile_pic= "http://127.0.0.1:8000/media/Title1_PAD36F9.png", 
            phone_number="02055555", 
            is_active=True, 
            owner_id=12)

        self.urls = '{url}?{filter}={value}&{filter1}={value1}&{filter2}={value2}'.format(
            url=reverse('profiles'),
            filter='depth', value='true', filter1='is_active', value1= 'true', filter2='user', value2='12')
        
        return super().setUp()
    
    def test_filter_profile(self):
        res = self.client.get(self.urls)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(self.create_data.first_name, 'best')
        self.assertEqual(self.create_data.last_name, 'tech')
        self.assertEqual(self.create_data.phone_number, '02055555')