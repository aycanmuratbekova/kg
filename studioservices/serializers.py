from rest_framework import serializers
from .models import Service, Props, ServiceImage


class PropsSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='get_category_display')
    various_props = serializers.CharField(source='get_various_props_display')

    class Meta:
        model = Props
        fields = "__all__"


class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        services = super(ServiceSerializer, self).to_representation(instance)
        if instance.images.exists():
            services['images'] = ServiceImageSerializer(instance.images.all(), many=True, context={'request': self.context.get('request')}).data
        return services

    class Meta:
        model = Service
        fields = "__all__"
