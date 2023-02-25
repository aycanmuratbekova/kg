from rest_framework import serializers
from .models import Location, LocationImage


class LocationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationImage
        fields = ['id', 'img']


class LocationSerializer(serializers.ModelSerializer):
    images = LocationImageSerializer(many=True)

    class Meta:
        model = Location
        fields = ['id', 'name', 'url_name', 'location', 'images']
