from rest_framework import serializers
from apps.winner.models import Winner


class LiveDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winner
        fields = '__all__'