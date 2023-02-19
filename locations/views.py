from rest_framework.viewsets import ModelViewSet
from .models import Location
from .serializers import LocationSerializer


class LocationViewSet(ModelViewSet):
    pagination_class = None
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
