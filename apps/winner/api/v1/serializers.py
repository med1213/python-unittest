from apps.candidate.models import Candidate
from apps.prize.models import Prize
from apps.bill.models import Bill
from apps.winner.models import Winner
from apps.village.models import Village
from apps.district.models import District
from apps.province.models import Province
from apps.period.models import Period
from rest_framework import serializers


class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = ['id', 'village',]
        read_only_fields = ['id', 'village']


class DistrictSerializers(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = ['id', 'district',]
        read_only_fields = ['id', 'district']


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'province',]
        ref_name = 'ProvinceAPI'
        read_only_fields = ['id', 'district']


class CandidateSerializers(serializers.ModelSerializer):
    province = ProvinceSerializer()
    district = DistrictSerializers()
    village = VillageSerializer()

    class Meta:
        model = Candidate
        fields = ['id', 'full_name', 'phone_number',
                  'village', 'district', 'province']


class PeriodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ['id', 'period',]


class LotteryBillSerializer(serializers.ModelSerializer):
    candidate = CandidateSerializers()
    period = PeriodSerializers()

    class Meta:
        model = Bill
        fields = ['id', 'bill_number', 'total_cost', 'image',
                  'device_number', 'candidate', 'period']


class PrizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prize
        fields = ['id', 'prize', 'detail']


class WinnerSerializer(serializers.ModelSerializer):
    lottery_bill = LotteryBillSerializer()
    prize = PrizeSerializer()

    class Meta:
        model = Winner
        fields = ['id', 'lottery_bill', 'prize',
                  'is_active']
        ref_name = 'WinnerProvinceAPI'


class WinnerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winner
        fields = ['id', 'lottery_bill', 'prize', 'is_active']
