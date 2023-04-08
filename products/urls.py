from django.urls import path

from . import views

urlpatterns = (
    path('category/get-all/', views.get_all_categories),
    path('product/get-top-sales', views.get_top_sale_products),
    path('product/get-latest', views.get_latest_products),
    path('product/search', views.search_products),
    path('product/get/<int:product_id>', views.get_product),
)