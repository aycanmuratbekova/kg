from django.urls import path
from .views import GlobalSearchView


urlpatterns = [
    path('global-search/', GlobalSearchView.as_view()),

]
