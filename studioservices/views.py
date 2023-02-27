from rest_framework import generics, filters
from rest_framework.response import Response

from .models import Props, Service, Pavilion, Transport, SourceMaterials
from .serializers import ServiceSerializer, PropsSerializer, PavilionSerializer, TransportSerializer, \
    SourceMaterialsSerializer


# class ServiceListView(generics.ListAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#
#     def list(self, request):
#         queryset = self.get_queryset()
#         serializer = ServiceSerializer(queryset, many=True, context={'request': request})
#         props_serializer = PropsSerializer(Props.objects.all(), many=True)
#
#         return Response({
#             'services': serializer.data,
#             'props': props_serializer.data,
#         })
#
#
# class ServiceDetailView(generics.RetrieveAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#
#
# class PropsDetailView(generics.RetrieveAPIView):
#     queryset = Props.objects.all()
#     serializer_class = PropsSerializer


# New code here

class PropsByCategoryView(generics.ListAPIView):
    filter_backends = [filters.SearchFilter]
    serializer_class = PropsSerializer

    def get_queryset(self):
        categories = {
            'mens-costumes': 1,
            'women-costumes': 2,
            'military-uniforms': 3,
            'various-props': 4,
        }
        category_id = 0
        try:
            category_id = categories[self.request.query_params.get('search')]
        except KeyError as err:
            print(f'\nReturning empty queryset\nKeyError : {err}\n')
        queryset = Props.objects.filter(category=category_id)
        return queryset


class PropsDetailView(generics.RetrieveAPIView):
    queryset = Props.objects.all()
    serializer_class = PropsSerializer


class ServiceByCategoryView(generics.ListAPIView):
    filter_backends = [filters.SearchFilter]
    serializer_class = ServiceSerializer

    def get_queryset(self):
        categories = {
            'working-with-an-image': 1,
            'working-with-sound': 2,
            'filming-equipment': 3,

        }
        category_id = 0
        try:
            category_id = categories[self.request.query_params.get('search')]
        except KeyError as err:
            print(f'\nReturning empty queryset\nKeyError : {err}\n')
        queryset = Service.objects.filter(category=category_id)
        return queryset


class ServiceDetailView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class PavilionListView(generics.ListAPIView):
    queryset = Pavilion.objects.all()
    serializer_class = PavilionSerializer


class PavilionDetailView(generics.RetrieveAPIView):
    queryset = Pavilion.objects.all()
    serializer_class = PavilionSerializer


class SourceMaterialsView(generics.ListAPIView):
    queryset = SourceMaterials.objects.all()
    serializer_class = SourceMaterialsSerializer


class TransportView(generics.ListAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer


