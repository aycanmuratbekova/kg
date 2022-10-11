import django_filters
from .models import Movie



class MovieFilter(django_filters.rest_framework.FilterSet):
    year__gte = django_filters.NumberFilter(field_name="year", method='filter_year__gte')
    year__lte = django_filters.NumberFilter(field_name="year", method='filter_year__lte')

    def filter_year__gte(self, queryset, name, value):
        return queryset.filter(year__gte=value)

    def filter_year__lte(self, queryset, name, value):
        return queryset.filter(year__lte=value)

    class Meta:
        model = Movie
        fields = [
            "id", "name", "duration",
            "year", "genre", "pg_rating", "description",
            "type", "kind", "footage", "audio",
            "restoration_year", "trailer",
            'year__gte', 'year__lte'
        ]
