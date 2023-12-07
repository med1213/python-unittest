from rest_framework import serializers
from apps.lucky_draw.models import LuckyDraw


class LuckyDrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuckyDraw
        fields = ['id', 'item_name', 'is_active', 'created_on', 'updated_on']
        # ordering = ['id']
