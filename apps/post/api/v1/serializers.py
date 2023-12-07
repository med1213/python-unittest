from rest_framework import serializers
from apps.post.models import Post


class PostGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        depth = 1

class PostPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'