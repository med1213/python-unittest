from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from apps.district.models import District
from apps.province.models import Province
from apps.village.models import Village
from django.contrib.auth.models import User

class VillageAPITestCase(APITestCase):

    def setUp(self):
        self.urls = reverse("villages")
        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin') 
    
    def test_view_posts(self):  # sourcery skip: class-extract-method
        self.test_province = Province.objects.create(
            id=1, province="Vientaince", is_active=True
        )
        self.test_district = District.objects.create(
            id=1, district="ໄຊທານີ", province_id=self.test_province.id, is_active=True
        )
        self.test_village = Village.objects.create(
            id=1, village="ban", district_id=self.test_district.id, is_active=True
        )

        response = self.client.get(self.urls, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['count'], int)
        self.assertEqual(response.data['count'],1)
        self.assertEqual(self.test_village.village, "ban")

    def test_get_detail_posts(self):
        url = self.test_data()
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.test_village.village, "ban")
        self.assertEqual(self.test_village.is_active, True)

    def test_create(self):
        self.test_provinc = Province.objects.create(id= 1,province= "Vientaince", is_active=True)
        self.test_district = District.objects.create(id= 1,district= "ໄຊທານີ", province_id= self.test_provinc.id, is_active=True)

        data = {"district" : 1, "village": "ban", "is_active": True,}

        response = self.client.post(self.urls, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['village'], data['village'])
        self.assertEqual(response.data['is_active'], data['is_active'])
        self.assertIsInstance(response.data['district'], int)
        self.assertEqual(response.data['district'], 1)

    def test_should_not_create_village_validate(self):

        self.test_province = Province.objects.create(id= 1,province= "Vientaince", is_active=True)
        self.test_district = District.objects.create(id= 1,district= "ໄຊທານີ", province_id= self.test_province.id, is_active=False)

        self.data = {"district" : 1, "village": "ban", "is_active": True,}

        response = self.client.post(self.urls, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.test_district.is_active, False)

    def test_update_village(self):
        url = self.test_data()
        data = {"district" : 1, "village": "donkoy", "is_active": True,}

        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['village'], data['village'])
        self.assertEqual(response.data['is_active'], data['is_active'])

    def test_delete_village(self):
        url = self.test_data()
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_data(self):
        self.test_province = Province.objects.create(
            id=1, province="Vientaince", is_active=True
        )
        self.test_district = District.objects.create(
            id=1, district="ໄຊທານີ", province_id=self.test_province.id, is_active=True
        )
        self.test_village = Village.objects.create(
            id=1, village="ban", district_id=self.test_district.id, is_active=True
        )
        return reverse('village', kwargs={'pk': 1})
    

class FilterVillageTestCase(APITestCase):

    def setUp(self) -> None:
        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin') 
        
        self.province = Province.objects.create(id=1, province="vientaince", is_active=True)
        self.district = District.objects.create(id=2, province_id=self.province.id, district="xaythany", is_active=True)
        self.village = Village.objects.create(id=1, village="donkoy", district_id=self.district.id, is_active=True)

        self.url = '{url}?{filter}={value}&{filter1}={value1}'.format(
            url=reverse('villages'),
            filter='is_active', value='true', filter1='depth', value1='true')
        

        self.village_url = '{url}?{filter}={value}'.format(
            url=reverse('villages'),
            filter='village', value='khamchang')        

        self.district_url = '{url}?{filter}={value}'.format(
            url=reverse('villages'),
            filter='district', value='2')

    def test_filter_village_by_status(self):
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.village.is_active, True)

    def test_filter_village_by_name(self):
        
        response = self.client.get(self.village_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.village.village, "donkoy")

    def test_filter_village_by_district(self):
        
        response = self.client.get(self.district_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)