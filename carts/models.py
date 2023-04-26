from django.db import models

from products.models import ProductDetail
from users.models import User


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
    product_detail = models.ForeignKey(to=ProductDetail, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)