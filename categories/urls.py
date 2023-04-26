from django.urls import path

from . import views

urlpatterns = (
    path('', views.get_all_categories),
    path('<int:category_id>', views.get_category),
)