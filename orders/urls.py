from django.urls import path

from . import views

urlpatterns = (
    path('add', views.add_order),
    path('get/<int:order_id>', views.get_order),
    path('get-by-user/<str:phone>', views.get_orders_by_user),
    path('update', views.update_order),
)