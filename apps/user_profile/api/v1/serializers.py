from rest_framework import serializers
from apps.user_profile.models import UserProfile


class UserProfileGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        depth = 1


class UserProfilePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UpdateUserprofileAdminSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField()

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'profile_pic',  'phone_number', 'gender')

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.profile_pic = validated_data.get('profile_pic', instance.profile_pic)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance