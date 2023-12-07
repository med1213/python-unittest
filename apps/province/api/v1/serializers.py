from rest_framework import serializers
from apps.province.models import Province


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'