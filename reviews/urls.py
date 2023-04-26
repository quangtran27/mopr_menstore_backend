from django.urls import path

from . import views

urlpatterns = (
    path('', views.add_review),
    path('<int:review_id>', views.get_review),
    path('<int:review_id>/images', views.get_review_images),
)