from django.contrib import admin
from .models import *


admin.site.register(Person)
admin.site.register(Compilation)


class PiMAdmin(admin.StackedInline):
    model = PersonInMovie
    extra = 1


class MICAdmin(admin.StackedInline):
    model = MovieInCompilation
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # model = Movie
    inlines = [PiMAdmin, MICAdmin]
    list_display = ['name', 'year', 'genre']


