from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken


class TestSetUp(APITestCase):        
    def setUp(self):
        # create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = self.get_token()
        self.refresh_token = self.get_refresh_token()
        self.verify_url = reverse('token_verify')
        self.url_refresh =reverse('token_refresh')
        self.url_blacklist = reverse('token_blacklist')

    def get_token(self):
        refresh = RefreshToken.for_user(self.user)
        return str(refresh.access_token)  
    
    def get_refresh_token(self):
        refresh = RefreshToken.for_user(self.user)
        return str(refresh)  