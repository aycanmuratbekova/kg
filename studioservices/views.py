from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class PropsCategeroyViewSet(ModelViewSet):
    queryset = PropsCategory.objects.all()
    serializer_class = PropsCategorySerializer


class PropsViewSet(ModelViewSet):
    queryset = Props.objects.all()
    serializer_class = PropsSerializer


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceCategoryViewSet(ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
