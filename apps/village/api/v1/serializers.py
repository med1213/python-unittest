from rest_framework import serializers
from apps.village.models import Village


class VillageGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Village
        fields = '__all__'
        depth = 2

class VillagePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Village
        fields = '__all__'


    def validate_district(self,value):
        if value.is_active == False:
            raise serializers.ValidationError('this district is not aviable')
        else:
            return value