from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class PropsViewSet(ModelViewSet):
    pagination_class = None
    queryset = Props.objects.all()
    serializer_class = PropsSerializer


class ServiceViewSet(ModelViewSet):
    pagination_class = None
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceCategoryViewSet(ModelViewSet):
    pagination_class = None
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
