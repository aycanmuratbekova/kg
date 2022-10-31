"""kyrgyzfilm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from news.views import NewsViewSet
from studioservices.views import PropsViewSet, PropsCategeroyViewSet


schema_view = get_schema_view(
    openapi.Info(
        #  add your swagger doc title
        title="Kyrgyz Film API",
        #  version of the swagger doc
        default_version='v1',
        # first line that appears on the top of the doc
        description="Click method buttons to get info",
    ),
    public=True,
)


router = routers.DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'props-category', PropsCategeroyViewSet)
router.register(r'props', PropsViewSet)


urlpatterns = [
    path('swagger/', schema_view.with_ui()),
    path('admin/', admin.site.urls),
    path('', include("art.urls")),
    path('', include(router.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
