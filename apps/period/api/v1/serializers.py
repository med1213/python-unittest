from rest_framework import serializers
from apps.period.models import Period


class PeriodGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Period
        fields = "__all__"
        depth = 3


class PeriodPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Period
        fields = "__all__"
