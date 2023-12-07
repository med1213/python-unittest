from rest_framework import serializers
from apps.district.models import District
from apps.province.models import Province


class DistrictGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = "__all__"
        depth = 1


class DistrictPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = District
        fields = "__all__"

    def validate_province(self,value):
        if value.is_active == False:
            raise serializers.ValidationError('this province is not aviable')
        else:
            return value