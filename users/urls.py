from django.urls import path

from . import views

urlpatterns = (
    path('login', views.login),
    path('register', views.register),
    path('<int:user_id>', views.get_user_info),
    path('<int:user_id>', views.update_user),
    path('<int:user_id>/password', views.change_password),
    path('<int:user_id>/orders', views.get_user_orders),
    path('<int:user_id>/cart', views.get_user_cart),
)