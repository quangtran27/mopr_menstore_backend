from django.urls import path

from . import views

urlpatterns = (
    path('', views.get_all_banners, name='Get all cart items'),
)