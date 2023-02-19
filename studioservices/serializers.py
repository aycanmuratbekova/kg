from rest_framework import serializers
from .models import *


class PropsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Props
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = "__all__"

