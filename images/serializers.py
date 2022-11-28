from rest_framework import serializers

from .models import ImageModel
from .models import TagModel


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = [
            'image_id',
            'tag',
        ]


class ImageSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = ImageModel
        fields = [
            'name',
            'description',
            'link',
            'tags',
        ]