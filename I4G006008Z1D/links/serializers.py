from rest_framework import serializers
from .models import Link
from django.contrib.auth.models import User


class LinkSerializer(serializers.Serializer):
    class Meta:
        model = Link
        fields = '__all__'
        