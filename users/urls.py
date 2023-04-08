from django.urls import path

from . import views

urlpatterns = (
    path('change-password', views.change_password),
    path('get/<str:phone>', views.get_user),
    path('login', views.login),
    path('register', views.register),
    path('update', views.update_user),
)