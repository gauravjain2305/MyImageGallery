from rest_framework import generics

from django.db import models
from .models import ImageModel, TagModel
from .serializers import ImageSerializer, TagSerializer


class ImageView(generics.ListAPIView):
    queryset = ImageModel.objects.all()
    # .prefetch_related(
    #         models.Prefetch(
    #             "Tags",
    #             queryset=TagModel.objects.filter(primary_placeholder=True)
    #         )
    serializer_class = ImageSerializer


class ImageCreateView(generics.CreateAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer

