from django.urls import path
from .views import ServiceDetailView, PropsDetailView, PropsByCategoryView, ServiceByCategoryView, \
    PavilionListView, PavilionDetailView, TransportView, SourceMaterialsView

urlpatterns = [

    path('props/', PropsByCategoryView.as_view()),
    path('props/<int:pk>/', PropsDetailView.as_view()),

    path('service/', ServiceByCategoryView.as_view()),
    path('service/<int:pk>/', ServiceDetailView.as_view()),

    path('pavilion/', PavilionListView.as_view()),
    path('pavilion/<int:pk>/', PavilionDetailView.as_view()),

    path('transport/', TransportView.as_view()),
    path('source-materials/', SourceMaterialsView.as_view()),

]
