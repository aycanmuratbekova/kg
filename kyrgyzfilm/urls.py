from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from news.views import NewsViewSet
from studioservices.views import PropsViewSet, PropsCategeroyViewSet, ServiceViewSet, ServiceCategoryViewSet
from locations.views import LocationViewSet


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
router.register(r'locations', LocationViewSet)
router.register(r'service-category', ServiceCategoryViewSet)
router.register(r'service', ServiceViewSet)


urlpatterns = [
    path('swagger/', schema_view.with_ui()),
    path('admin/', admin.site.urls),
    path('core/', include("core.urls")),
    path('', include("art.urls")),
    path('', include(router.urls)),
    path('contact/', include("contact_form.urls")),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
