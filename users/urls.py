from django.urls import path

from . import views

urlpatterns = (
    path('login', views.login),
    path('register', views.register),
    path('staff-login', views.staff_login),
    path('<int:user_id>', views.get_or_update_user),
    path('<int:user_id>/password', views.change_password),
    path('<int:user_id>/orders', views.get_user_orders),
    path('<int:user_id>/notifications', views.get_user_notifications),
    path('<int:user_id>/cart', views.get_user_cart),
)