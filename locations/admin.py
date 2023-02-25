from django.contrib import admin
from .models import Location, LocationImage


# admin.site.register(Location)


class LocationImageInlineAdmin(admin.StackedInline):
    model = LocationImage
    extra = 1


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [LocationImageInlineAdmin, ]
    list_display = ['name', 'url_name', 'location']


