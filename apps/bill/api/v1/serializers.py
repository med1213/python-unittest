from rest_framework import serializers
from apps.bill.models import Bill


class LotteryGetBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'
        # depth = 2


class LotteryPostBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'
