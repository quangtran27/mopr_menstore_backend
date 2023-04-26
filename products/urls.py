from django.urls import path

from . import views

urlpatterns = (
    path('', views.get_all_products),
    path('<int:product_id>', views.get_product),
    path('<int:product_id>/details', views.get_product_details),
    path('details/<int:product_detail_id>', views.get_product_detail),
    path('<int:product_id>/images', views.get_product_images),
    path('<int:product_id>/reviews', views.get_product_reviews),
    path('top-sales', views.get_top_sale_products),
    path('latest', views.get_latest_products),
    path('search', views.search_products),

)