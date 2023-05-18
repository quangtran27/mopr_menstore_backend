from django.db import models

from orders.models import Order
from users.models import User


class Notification(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  order = models.ForeignKey(Order, on_delete=models.PROTECT)
  title = models.CharField(max_length=512)
  body = models.TextField()
  is_checked = models.BooleanField(default=False)
  created = models.DateTimeField(auto_now_add=True)