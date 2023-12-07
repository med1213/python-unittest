from rest_framework import serializers
from apps.prize_type.models import PrizeType


class PrizeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrizeType
        fields = '__all__'
