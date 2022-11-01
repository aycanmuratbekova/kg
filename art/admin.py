from django.contrib import admin
from .models import *


admin.site.register(Person)


class PiMAdmin(admin.StackedInline):
    model = PersonInMovie
    extra = 1

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # model = Movie
    inlines = [PiMAdmin]
    list_display = ['name', 'year', 'genre']


