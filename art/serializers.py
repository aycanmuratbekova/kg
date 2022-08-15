from rest_framework import serializers
from .models import Movie, PersonInMovie, Person


class PersonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name', 'second_name']


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
            'name',
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
