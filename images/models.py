from django.db import models


class ImageModel(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    link = models.URLField(max_length=500)


class TagModel(models.Model):
    image_model = models.ForeignKey(ImageModel, related_name='tags', on_delete=models.CASCADE)
    tag = models.CharField(max_length=200)
