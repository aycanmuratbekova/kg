from rest_framework import generics
from rest_framework.response import Response

from .models import Props, Service, ServiceCategory
from .serializers import ServiceSerializer, PropsSerializer


class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ServiceSerializer(queryset, many=True, context={'request': request})
        props_serializer = PropsSerializer(Props.objects.all(), many=True)

        return Response({
            'services': serializer.data,
            'props': props_serializer.data,
        })


class ServiceDetailView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class PropsDetailView(generics.RetrieveAPIView):
    queryset = Props.objects.all()
    serializer_class = PropsSerializer




