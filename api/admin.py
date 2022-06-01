from django.contrib import admin
from .models import Image

# Register your models here.


@admin.register(Image)
class ImagesModel(admin.ModelAdmin):
    list_filter = ('title', 'batch_num', 'image')
    list_display = ('title', 'batch_num', 'image')