from rest_framework import serializers
from .models import Image


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'title', 'batch_num', 'image']