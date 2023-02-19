from django.contrib import admin
from .models import *


admin.site.register(Props)


class ServiceImageInline(admin.StackedInline):
    model = ServiceImage
    extra = 1


class ServiceCategoryInline(admin.StackedInline):
    model = ServiceCategory
    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceImageInline, ServiceCategoryInline]

    class Meta:
        model = Service
