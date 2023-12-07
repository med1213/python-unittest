from rest_framework import serializers
from apps.period_type.models import PeriodType


class PeriodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodType
        fields = '__all__'
