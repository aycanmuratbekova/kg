from rest_framework import serializers
from .models import *


class PropsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PropsCategory
        fields = "__all__"


class PropsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Props
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

