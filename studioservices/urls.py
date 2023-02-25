from django.urls import path
from .views import ServiceListView, ServiceDetailView, PropsDetailView

urlpatterns = [
    path('service/', ServiceListView.as_view()),
    path('service/<int:pk>/', ServiceDetailView.as_view()),
    path('props/<int:pk>/', PropsDetailView.as_view()),

]
