from rest_framework import serializers
from .models import *


# class MovieListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ["name", "poster", "year", "genre"]


class MovieListForCompilationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='movie.id')
    name = serializers.StringRelatedField(many=False)
    url_name = serializers.StringRelatedField(many=False)
    year = serializers.IntegerField(source="movie.year")
    poster = serializers.ImageField(source="movie.poster")
    genre = serializers.CharField(source='movie.genre')

    class Meta:
        model = MovieInCompilation
        fields = ["id", "name", 'url_name', 'year', 'genre', 'poster']


class CompilationSerializer(serializers.ModelSerializer):
    movie_in_compilation = MovieListForCompilationSerializer(many=True)

    class Meta:
        model = Compilation
        fields = ["id", 'name', 'url_name', "movie_in_compilation"]


class MovieListForPersonSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="movie.id")
    movie = serializers.StringRelatedField(many=False)
    year = serializers.IntegerField(source="movie.year")
    profession = serializers.CharField(source='get_profession_display')

    class Meta:
        model = PersonInMovie
        fields = ["id", "year", 'movie', 'profession']


class PersonSerializer(serializers.ModelSerializer):
    movies = MovieListForPersonSerializer(many=True)

    class Meta:
        model = Person
        fields = [
            "id",
            "first_name",
            "second_name",
            "url_name",
            "profession",
            "bio",
            "photo",
            "movies",
        ]


class PersonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name', 'second_name', 'url_name']


class PersonInMovieSerializer(serializers.ModelSerializer):
    person = serializers.StringRelatedField(many=False)
    profession = serializers.CharField(source='get_profession_display')

    class Meta:
        model = PersonInMovie
        fields = ['profession', 'person']


class MovieSerializer(serializers.ModelSerializer):
    persons = PersonInMovieSerializer(many=True)

    class Meta:
        model = Movie
        fields = [
            'id',
            'name',
            'url_name',
            'duration',
            'year',
            'genre',
            'pg_rating',
            'description',
            'type',
            'kind',
            'footage',
            'audio',
            'restoration_year',
            'poster',
            'trailer',
            "persons",
        ]
