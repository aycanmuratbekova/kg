from rest_framework import serializers
from .models import *


# class MovieListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ["name", "poster", "year", "genre"]


class MovieListForCompilationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='movie.id')
    name = serializers.StringRelatedField(source="movie.name")
    url_name = serializers.StringRelatedField(source="movie.url_name")
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
    profession = serializers.StringRelatedField(many=False)

    class Meta:
        model = PersonInMovie
        fields = ["id", "year", 'movie', 'profession']


class ProfessionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    url_name = serializers.CharField()
    profession_group_id = serializers.IntegerField(source="profession_group.id")
    profession_group = serializers.StringRelatedField(many=False)
    profession_group_url_name = serializers.StringRelatedField(source="profession_group.url_name")

    class Meta:
        model = PersonInMovie
        fields = ["id", 'name', 'url_name', "profession_group_id", "profession_group", "profession_group_url_name"]


class PersonSerializer(serializers.ModelSerializer):
    movies = MovieListForPersonSerializer(many=True)
    gender = serializers.CharField(source='get_gender_display')
    assistant = serializers.CharField(source='get_assistant_display')
    # profession = serializers.StringRelatedField(many=False)
    profession = ProfessionSerializer(many=False)

    class Meta:
        model = Person
        fields = [
            "id",
            "first_name",
            "second_name",
            "url_name",
            "gender",
            "age",
            "profession",
            "appearance",
            "assistant",
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
    profession = serializers.StringRelatedField(many=False)

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
