from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   re_path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('banners/', include('banners.urls')),
    path('carts/', include('carts.urls')),
    path('categories/', include('categories.urls')),
    path('orders/', include('orders.urls')),
    path('notifications/', include('notifications.urls')),
    path('', include('products.urls')),
    path('reviews/', include('reviews.urls')),
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
