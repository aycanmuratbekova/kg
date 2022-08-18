from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Movie, Person
from .serializers import MovieSerializer, PersonSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer