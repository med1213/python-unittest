from rest_framework import status
from .test_setup import TestSetUp

class TestView(TestSetUp):

    def test_verify_token(self):
        data = {"token": self.token}
        response = self.client.post(self.verify_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_refresh_token_with_valid_token(self):        
        data = {
            "refresh": self.refresh_token
        }
        response = self.client.post(self.url_refresh, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_blacklist_token_on_logout(self):        
        data = {
            "refresh": self.refresh_token
        }
        response = self.client.post(self.url_blacklist, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
