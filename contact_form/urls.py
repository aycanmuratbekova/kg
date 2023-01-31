from django.urls import path
from .views import ContactAPIView, OrderServiceAPIView

urlpatterns = [
    path('contact/', ContactAPIView.as_view()),
    path('order-service/', OrderServiceAPIView.as_view()),
]
