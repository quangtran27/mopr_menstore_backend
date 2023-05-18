from django.urls import path

from . import views

urlpatterns = (
    path('<int:notification_id>', views.update_notification),
)