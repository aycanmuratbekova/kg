from django.contrib import admin
from .models import Props, Service, ServiceImage, Pavilion, PavilionImage, Transport, TransportImage


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


class TransportImageInline(admin.StackedInline):
    model = TransportImage
    extra = 1


@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    inlines = [TransportImageInline, ]

    def has_add_permission(self, request, obj=None):
        has_permission = True
        has_transport = Transport.objects.all()
        if has_transport:
            has_permission = False

        return has_permission

    class Meta:
        model = Transport
