from apps.bill.models import Bill
from apps.candidate.models import Candidate
from apps.prize_type.models import PrizeType
from apps.province.models import Province
from apps.district.models import District
from apps.village.models import Village
from apps.period.models import Period
from apps.prize.models import Prize
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

from apps.winner.models import Winner

class WinnerAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.win_urls = reverse("winners")    
        self.win_url = reverse("winner", kwargs={'pk': 2})

        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin') 


        self.prize_data = PrizeType.objects.create(id=1, prize_type='big', is_active=True)
        self.prize_data = Prize.objects.create(id=1, prize='moto', detail='moto', quantity='1', is_active=True, prize_type_id=1)

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
                                                 open_date="2023-04-06",
                                                 close_date="2023-04-06",
                                                 is_active=True)

        self.bill_data = Bill.objects.create(
            id=1,
            bill_number='4567895123549',
            total_cost='50000',
            image="http://127.0.0.1:8000/media/Title1_PAD36F9.png",
            is_draw=False,
            device_number='12345678',
            is_active=True,
            candidate_id=1,
            period_id=1,

        )

        self.winner_data = Winner.objects.create(
            id=2,
            is_active=True,
            lottery_bill_id=1,
            prize_id=1,

        )

        self.win_data = {
            "is_active": True,
            "lottery_bill": 1,
            "prize": 1,

        }

    def test_get_all(self):

        response = self.client.get(self.win_urls,)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data['count'], int)
        self.assertEqual(response.data['count'], 1)

    def test_create(self):

        response = self.client.post(self.win_urls, self.win_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_update(self):
    #     data = {"prize": 1, "lottery_bill" : 1,"is_active": True,}

    #     print("===self.win_url===", self.win_url)

    #     response = self.client.patch(self.win_url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):

        response = self.client.delete(self.win_url, )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class FilterPeriodAPITestCase(APITestCase):
    def setUp(self) -> None:

        self.testuser1 = User.objects.create_superuser(
            username='admin', password='admin')

        self.client.login(username=self.testuser1.username,
                          password='admin') 

        self.prize_data = PrizeType.objects.create(id=1, prize_type='big', is_active=True)
        self.prize_data = Prize.objects.create(id=1, prize='moto', detail='moto', quantity='1', is_active=True, prize_type_id=1)
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
                                                 open_date="2023-04-06",
                                                 close_date="2023-04-06",
                                                 is_active=True)

        self.bill_data = Bill.objects.create(
            id=1,
            bill_number='4567895123549',
            total_cost='50000',
            image="http://127.0.0.1:8000/media/Title1_PAD36F9.png",
            is_draw=False,
            device_number='12345678',
            is_active=True,
            candidate_id=1,
            period_id=1,

        )

        self.winner_data = Winner.objects.create(
            id=2,
            is_active=True,
            lottery_bill_id=1,
            prize_id=1,

        )

        self.urls = '{url}?{filter}={value}&{filter1}={value1}&{filter2}={value2}'.format(
            url=reverse('winners'),
            filter='related_id', value='true', filter1='period', value1='1', filter2='prize', value2='1')

        return super().setUp()

    def test_filter_winner(self):
        res = self.client.get(self.urls)
        self.assertEqual(res.status_code, status.HTTP_200_OK)