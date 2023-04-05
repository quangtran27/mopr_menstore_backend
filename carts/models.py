from django.db import models

from products.models import Product
from users.models import User


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    pass

class CartItem(models.Model):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)