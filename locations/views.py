from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import Location
from .serializers import LocationSerializer


class LocationViewSet(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
