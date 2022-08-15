from django.db import models
from .person import Person
from .profession import PROFESSIONS


class Movie(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название фильма')
    duration = models.DurationField(verbose_name='Длительность')
    year = models.PositiveIntegerField(verbose_name="Год выпуска")
    genre = models.CharField(max_length=255, verbose_name="Жанр")
    pg_rating = models.PositiveIntegerField(default=0, verbose_name="Возрастное ограничение")
    description = models.TextField(verbose_name="Описание фильма")
    type = models.CharField(max_length=255, verbose_name="Тип фильма")
    kind = models.CharField(max_length=255, verbose_name="Вид фильма")
    footage = models.CharField(max_length=255, verbose_name="Метраж")
    audio = models.CharField(max_length=255, verbose_name="Звук")
    restoration_year = models.PositiveIntegerField(null=True, blank=True, verbose_name='Год восстановления')
    poster = models.ImageField(upload_to='movie', null=True, blank=False, verbose_name="Постер фильма")
    trailer = models.URLField(verbose_name="Ссылка на трейлер в Youtube", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class PersonInMovie(models.Model):
    movie = models.ForeignKey(to=Movie, on_delete=models.SET_NULL, null=True, blank=True, related_name='persons')
    person = models.ForeignKey(to=Person, on_delete=models.SET_NULL, null=True, blank=True)
    profession = models.IntegerField(default=5, choices=PROFESSIONS)

    def __str__(self):
        return f"{self.get_profession_display()} - {self.person}"

    class Meta:
        verbose_name = 'Участник фильма'
        verbose_name_plural = 'Участники фильма'

