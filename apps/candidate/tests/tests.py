from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from apps.candidate.models import Candidate
from apps.province.models import Province
from apps.district.models import District
from apps.village.models import Village
from django.contrib.auth.models import User


class CreateTestCandidate(APITestCase):

    def setUp(self):
        self.urls = reverse('candidates')
        self.url = reverse('candidate', kwargs={'pk': 2})

        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
        
        self.province = Province.objects.create(
            id=1, province="vientaince", is_active=True
        )
        self.district_data = District.objects.create(
            id=1, province_id=1, district="xaythany", is_active=True
        )
        self.village_data = Village.objects.create(
            id=1, district_id=1, village="village", is_active=True
        )
        self.candidate_data = Candidate.objects.create(
            id=2,  
            province_id=1,  
            district_id=1,  
            village_id=1,  
            full_name="full_name",
            phone_number="12345678", 
            is_active=True
        )

        self.data = {
            "province": 1,
            "district": 1,
            "village": 1,
            "full_name": "John",
            "phone_number": "2098989898",
            "is_active": True
        }

    def test_get_all(self):

        response = self.client.get(self.urls,)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['count'], int)
        self.assertEqual(response.data['count'],1)
        self.assertEqual(self.candidate_data.full_name, "full_name")

    def test_get_one(self):
        response = self.client.get(self.url,)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.candidate_data.full_name, "full_name")

    def test_create(self):

        response = self.client.post(self.urls, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['full_name'], self.data['full_name'])

    def test_update(self):

        response = self.client.patch(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name'], self.data['full_name'])

    def test_delete(self):

        response = self.client.delete(self.url, )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class FilterUsercandidateAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')

        self.province = Province.objects.create(
            id=1, province="vientaince", is_active=True
        )
        self.district_data = District.objects.create(
            id=1, province_id=1, district="xaythany", is_active=True
        )
        self.village_data = Village.objects.create(
            id=1, district_id=1, village="village", is_active=True
        )
        self.candidate_data = Candidate.objects.create(
            id=2,  
            province_id=1,  
            district_id=1,  
            village_id=1,  
            full_name="full_name",
            phone_number="12345678", 
            is_active=True
        )

        self.urls = '{url}?{filter}={value}&{filter1}={value1}&{filter2}={value2}'.format(
            url=reverse('candidates'),
            filter='depth', value='true', filter1='is_active', value1= 'true', filter2='phone_number', value2='12345678')
        
        return super().setUp()
    
    def test_filter_candidate(self):
        res = self.client.get(self.urls)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(self.candidate_data.full_name, 'full_name')
        self.assertEqual(self.candidate_data.phone_number, '12345678')