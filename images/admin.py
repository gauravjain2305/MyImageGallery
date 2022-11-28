from django.contrib import admin

# Register your models here.
from .models import ImageModel, TagModel

admin.site.register(ImageModel)