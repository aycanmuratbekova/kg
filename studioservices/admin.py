from django.contrib import admin
from .models import Props, Service, ServiceImage, Pavilion, PavilionImage


admin.site.register(Props)


class ServiceImageInline(admin.StackedInline):
    model = ServiceImage
    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceImageInline, ]

    class Meta:
        model = Service


# New Table

class PavilionImageInline(admin.StackedInline):
    model = PavilionImage
    extra = 1


@admin.register(Pavilion)
class PavilionAdmin(admin.ModelAdmin):
    inlines = [PavilionImageInline, ]

    class Meta:
        model = Pavilion
