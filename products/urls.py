from django.urls import path

from . import views

urlpatterns = (
    path('products/', views.get_all_products),
    path('products/<int:product_id>', views.get_or_update_product),
    path('products/<int:product_id>/details', views.get_product_details),
    path('products/details/<int:product_detail_id>', views.get_product_detail),
    path('products/<int:product_id>/images', views.get_product_images),
    path('products/<int:product_id>/reviews', views.get_product_reviews),
    path('products/top-sales', views.get_top_sale_products),
    path('products/latest', views.get_latest_products),

    # # Test
    # path('api/products', views.get_all_products_api),
    # path('api/products/top-sales', views.get_top_sales_products_api),
)