from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'person', PersonViewSet)
router.register(r'compilation', CompilationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
