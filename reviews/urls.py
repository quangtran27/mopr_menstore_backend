from django.urls import path

from . import views

urlpatterns = (
    path('get-by-product/<int:product_id>', views.get_reviews_by_product),
    path('add', views.add_review),
)