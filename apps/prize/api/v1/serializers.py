from rest_framework import serializers
from apps.prize.models import Prize


class PrizeGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prize
        fields = '__all__'
        depth = 1


class PrizePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prize
        fields = '__all__'
