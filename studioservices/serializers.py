from rest_framework import serializers
from .models import Service, Props, ServiceImage, Pavilion, PavilionImage, SourceMaterials, SourceMaterialsImage,\
    Transport, TransportImage


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


class PavilionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PavilionImage
        fields = "__all__"


class PavilionSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        pavilion = super(PavilionSerializer, self).to_representation(instance)
        if instance.images.exists():
            pavilion['images'] = PavilionImageSerializer(instance.images.all(), many=True, context={'request': self.context.get('request')}).data
        return pavilion

    class Meta:
        model = Pavilion
        fields = "__all__"


class SourceMaterialsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceMaterialsImage
        fields = "__all__"


class SourceMaterialsSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        source_materials = super(SourceMaterialsSerializer, self).to_representation(instance)
        if instance.images.exists():
            source_materials['images'] = SourceMaterialsImageSerializer(instance.images.all(), many=True, context={'request': self.context.get('request')}).data
        return source_materials

    class Meta:
        model = SourceMaterials
        fields = "__all__"


class TransportImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportImage
        fields = "__all__"


class TransportSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        transport = super(TransportSerializer, self).to_representation(instance)
        if instance.images.exists():
            transport['images'] = TransportImageSerializer(instance.images.all(), many=True, context={'request': self.context.get('request')}).data
        return transport

    class Meta:
        model = Transport
        fields = "__all__"
