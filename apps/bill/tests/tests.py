from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from apps.bill.models import Bill
from apps.candidate.models import Candidate
from apps.period.models import Period
from apps.province.models import Province
from apps.district.models import District
from apps.village.models import Village
import io
from PIL import Image
from django.contrib.auth.models import User


class BillAPITestCase(APITestCase):
    def setUp(self):
        self.bill_urls = reverse('bills')
        self.bill_url = reverse('bill', kwargs={'pk': 2})

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
            id=1,
            province_id=1,
            district_id=1,
            village_id=1,
            full_name="full_name",
            phone_number="12345678",
            is_active=True
        )
        self.period_data = Period.objects.create(id=1,
                                                 period="1",
                                                 #  prize_type=[1],
                                                 #  period_type=[1],
                                                 open_date="2023-04-06",
                                                 close_date="2023-04-06",
                                                 is_active=True)

        self.bill_data = Bill.objects.create(
            id=2,
            bill_number='4567895123549',
            total_cost='50000',
            image="http://127.0.0.1:8000/media/Title1_PAD36F9.png",
            is_draw=False,
            device_number='12345678',
            is_active=True,
            candidate_id=1,
            period_id=1,

        )

        photo_file = self.generate_photo_file()
        self.data = {
            "bill_number": '4567895123549',
            "total_cost": 50000,
            "image": photo_file,
            "is_draw": False,
            "device_number": 12345678,
            "is_active": True,
            "candidate": 1,
            "period": 1,

        }

    def test_get_all(self):

        response = self.client.get(self.bill_urls,)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['count'], int)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(self.bill_data.bill_number, "4567895123549")
        self.assertEqual(self.bill_data.device_number, "12345678")
        self.assertEqual(self.bill_data.total_cost, "50000")

    def test_get_one(self):
        response = self.client.get(self.bill_url,)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.bill_data.bill_number, "4567895123549")
        self.assertEqual(self.bill_data.device_number, "12345678")
        self.assertEqual(self.bill_data.total_cost, "50000")

    def test_create(self):

        response = self.client.post(
            self.bill_urls, self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data['bill_number'], self.data['bill_number'])
        self.assertIsInstance(response.data['total_cost'], int)
        self.assertEqual(response.data['total_cost'], self.data['total_cost'])
        self.assertIsInstance(response.data['device_number'], int)
        self.assertEqual(
            response.data['device_number'], self.data['device_number'])

    def test_update(self):

        response = self.client.patch(
            self.bill_url, self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['bill_number'], self.data['bill_number'])
        self.assertIsInstance(response.data['total_cost'], int)
        self.assertEqual(response.data['total_cost'], self.data['total_cost'])
        self.assertIsInstance(response.data['device_number'], int)
        self.assertEqual(
            response.data['device_number'], self.data['device_number'])

    def test_delete(self):

        response = self.client.delete(self.bill_url, )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file


class FilterBillAPITestCase(APITestCase):
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
            id=1,
            province_id=1,
            district_id=1,
            village_id=1,
            full_name="full_name",
            phone_number="12345678",
            is_active=True
        )
        self.period_data = Period.objects.create(id=1,
                                                 period="1",
                                                 #  prize_type=[1],
                                                 #  period_type=[1],
                                                 open_date="2023-04-06",
                                                 close_date="2023-04-06",
                                                 is_active=True)

        self.bill_data = Bill.objects.create(
            id=2,
            bill_number='4567895123549',
            total_cost='50000',
            image="http://127.0.0.1:8000/media/Title1_PAD36F9.png",
            is_draw=False,
            device_number='12345678',
            is_active=True,
            candidate_id=1,
            period_id=1,

        )

        self.urls = '{url}?{filter}={value}&{filter1}={value1}&{filter2}={value2}'.format(
            url=reverse('bills'),
            filter='depth', value='true', filter1='is_draw', value1='false', filter2='period', value2='1',)

    def test_filter_bill(self):
        res = self.client.get(self.urls)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIsInstance(res.data['count'], int)
        self.assertEqual(res.data['count'], 1)
        self.assertEqual(self.bill_data.bill_number, "4567895123549")
        self.assertEqual(self.bill_data.device_number, "12345678")
        self.assertEqual(self.bill_data.total_cost, "50000")
