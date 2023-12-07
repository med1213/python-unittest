from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from apps.province.models import Province
from ..models import District
from django.contrib.auth.models import User


class DistrictTestCase(APITestCase):

    def setUp(self):

        self.url = reverse("districts")
        self.test_province = Province.objects.create(id= 2, province='abd',)
        self.data = {"province": 2, "district": "xaythany", "is_active": "true"}
        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')

    def test_view_posts(self):
        self.province = Province.objects.create(
            id=1, province="vientaince", is_active=True
        )
        self.district_data = District.objects.create(
            id=1, province_id=1, district="xaythany", is_active=True
        )
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['count'], int)
        self.assertEqual(response.data['count'],1)
        self.assertEqual(self.district_data.district, "xaythany")

    def test_get_detail_posts(self):        
        urls = self._data_test()
        response = self.client.get(urls, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.district_data.district, "xaythany")
        self.assertEqual(self.district_data.is_active, True)

    def test_create_district(self):
        self.test_province = Province.objects.create(id=1, province="vientaince", is_active=True)
        data = {"province": 1, "district": "xaythany", "is_active": True}

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['district'], data['district'])
        self.assertEqual(response.data['is_active'], data['is_active'])

    def test_should_not_create_district_validate(self):

        self.test_province = Province.objects.create(id=1, province="vientaince", is_active=False)
        self.data = {"province": 1, "district": "xaythany", "is_active": "true"}

        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.test_province.is_active, False)

    def test_update(self):
        url = self._data_test()
        data={"province": 1, "district": "xaythany", "is_active": True}

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['district'], data['district'])
        self.assertEqual(response.data['is_active'], data['is_active'])

    def test_delete(self):
        url = self._data_test()
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def _data_test(self):
        self.province = Province.objects.create(
            id=1, province="vientaince", is_active=True
        )
        self.district_data = District.objects.create(
            id=1, province_id=1, district="xaythany", is_active=True
        )
        return reverse("district", kwargs={'pk': 1})
    
class DistrictFilterAPITestCase(APITestCase):

    def setUp(self) -> None:
        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin')
        self.province = Province.objects.create(id=1, province="vientaince", is_active=True)
        self.district = District.objects.create(id=1, province_id=1, district="xaythany", is_active=True)
        self.district = District.objects.create(id=2, province_id=1, district="pakse", is_active=True)

        self.district_url = '{url}?{filter}={value}'.format(
            url=reverse('districts'),
            filter='district', value='xaythany')        

        self.province_url = '{url}?{filter}={value}'.format(
            url=reverse('districts'),
            filter='province', value='1')
        
        self.urls = '{url}?{filter}={value}&{filter1}={value1}&{filter2}={value2}'.format(
            url=reverse('districts'),
            filter='depth', value='true', filter1='is_active', value1= 'true', filter2='', value2='')

    def test_filter_district_by_is_active(self):
        
        response = self.client.get(self.urls)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.district.is_active, True)

    def test_filter_district_by_name(self):
        
        response = self.client.get(self.district_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(self.district.district, 'xaythany')

    def test_filter_district_by_province(self):
        
        response = self.client.get(self.province_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
