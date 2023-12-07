
from rest_framework import serializers
from django.contrib.auth.models import User


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True,)
    confirm_password = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'confirm_password')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
    

class AdminChangeUserPasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True,)

    class Meta:
        model = User
        fields = ('password',)

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
