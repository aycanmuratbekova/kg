from django.contrib import admin
from .models import *


admin.site.register(PropsCategory)
admin.site.register(Props)


class ServiceImageAdmin(admin.StackedInline):
    model = ServiceImage
    extra = 1


class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceImageAdmin]

    class Meta:
        model = Service


admin.site.register(ServiceImage)
admin.site.register(Service, ServiceAdmin)




