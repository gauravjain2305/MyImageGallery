from rest_framework import generics
from rest_framework.response import Response

from .models import ImageModel
from .serializers import ImageSerializer, TagSerializer


class ImageView(generics.ListAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer


class ImageCreateView(generics.CreateAPIView):
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        image_serializer = ImageSerializer(data=request.data)
        if image_serializer.is_valid(raise_exception=True):
            image_instance = image_serializer.save()
            for data in request.data.get('tags'):
                tag_data = {
                    "image_model": image_instance.id,
                    "tag": data
                }
                tag_serializer = TagSerializer(data=tag_data)
                if tag_serializer.is_valid(raise_exception=True):
                    tag_serializer.save()
        return Response(image_serializer.data)