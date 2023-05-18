from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
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
