from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Movie, Person
from .serializers import MovieSerializer, PersonSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "id", "name", "duration",
        "year", "genre", "pg_rating", "description",
        "type", "kind", "footage", "audio",
        "restoration_year", "trailer"
    ]


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "id", "first_name", "second_name",
        "profession", "bio"
    ]
