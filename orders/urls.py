from django.urls import path

from . import views

urlpatterns = (
    path('', views.add_or_get_all_orders),
    path('<int:order_id>', views.get_or_update_order),
    path('<int:order_id>/items', views.get_order_items),
)