from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class PropsCategeroyViewSet(ModelViewSet):
    queryset = PropsCategory.objects.all()
    serializer_class = PropsCategorySerializer


class PropsViewSet(ModelViewSet):
    queryset = Props.objects.all()
    serializer_class = PropsSerializer
