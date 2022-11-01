from django.db import models
from .movie import Movie


class Compilation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название подборки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подбока"
        verbose_name_plural = "Подборки"


class MovieInCompilation(models.Model):
    movie = models.ForeignKey(Movie, models.CASCADE, 'movie_in_compilation')
    compilation = models.ForeignKey(Compilation, models.CASCADE, 'movie_in_compilation')

    def __str__(self):
        return f"{self.compilation.name} - {self.movie.name}"

    class Meta:
        verbose_name = "Фильм в подбоке"
        verbose_name_plural = "Фильмы в подбоках"
