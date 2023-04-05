from django.urls import path

from . import views

urlpatterns = (
    path('category/get-all/', views.get_all_categories),

    # product
    path('product/get-all', views.get_all_products),
    path('product/get/<int:product_id>', views.get_product)
)