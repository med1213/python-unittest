from rest_framework import serializers
from apps.slide.models import Slide


class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = '__all__'