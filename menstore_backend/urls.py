from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('products.urls')),
    path('admin/', admin.site.urls),
    path('cart/', include('carts.urls')),
    path('order/', include('orders.urls')),
    path('review/', include('reviews.urls')),
    path('user/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
