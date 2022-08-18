from django.urls import path, include
from rest_framework import routers
from .views import MovieViewSet, PersonViewSet


router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'person', PersonViewSet)

urlpatterns = [
    path('', include(router.urls))
]