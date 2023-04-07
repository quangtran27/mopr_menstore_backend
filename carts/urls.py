from django.urls import path

from . import views

urlpatterns = (
    path('add-to-cart', views.add_to_cart),
    path('get-by-user/<str:phone>', views.get_cart_by_user),
    path('update', views.update_cart)
)