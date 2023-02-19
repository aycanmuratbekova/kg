from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .models import Movie, Person
from .serializers import *
from .filters import MovieFilter


class MovieViewSet(ModelViewSet):
    pagination_class = None
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = MovieFilter
    search_fields = ['name']


class PersonViewSet(ModelViewSet):
    pagination_class = None
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = [
        "id", "first_name", "second_name",
        "profession", "bio"
    ]
    search_fields = ['first_name', 'second_name']


class CompilationViewSet(ModelViewSet):
    pagination_class = None
    queryset = Compilation.objects.all()
    serializer_class = CompilationSerializer
