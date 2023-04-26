from django.urls import path

from . import views

urlpatterns = (
    path('<int:cart_id>', views.get_cart),
    path('<int:cart_id>/items', views.get_or_add_cart_items),
    path('<int:cart_id>/items/<int:cart_item_id>', views.update_or_delete_cart_item),
)