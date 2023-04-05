from django.urls import path

from . import views

urlpatterns = (
    path('user/register/', views.user_register),
    # path('user/login/', views.user_login),
    # path('user/logout/', views.user_logout),
)