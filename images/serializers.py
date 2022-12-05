from rest_framework import serializers

from .models import ImageModel, TagModel


class ImageSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='tag')

    class Meta:
        model = ImageModel
        fields = [
            'name',
            'description',
            'link',
            'tags',
        ]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = [
            'image_model',
            'tag',
        ]