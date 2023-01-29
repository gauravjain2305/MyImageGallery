from rest_framework import serializers
from django.contrib.auth.models import User

from .models import ImageModel, TagModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class ImageSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='tag')

    class Meta:
        model = ImageModel
        fields = [
            'id',
            'name',
            'description',
            'link',
            'tags'
        ]

    # def get_tags(self, obj):
    #     qs = TagModel.objects.filter(image_model = obj.id)
    #     return TagSerializer(qs, many=True).data

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = [
            'image_model',
            'tag'
        ]