from django.db import models

from products.models import ProductDetail
from users.models import User

ORDER_STATUS = ((1, 'Created'), (2, 'Delivering'), (3, 'Delivered'), (4, 'Cancelled'))
ORDER_PAYMENT = ((1, 'COD'), (2, 'Banking'), (3, 'Others'))

class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField()
    status = models.IntegerField(choices=ORDER_STATUS)
    name = models.CharField(max_length=200, default='Customer Name')
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    payment = models.IntegerField(choices=ORDER_PAYMENT)
    is_paid = models.BooleanField(default=False)
    note = models.TextField()
    total = models.PositiveIntegerField()

class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product_detail = models.ForeignKey(to=ProductDetail, on_delete=models.PROTECT)
    on_sale = models.BooleanField(default=False)
    price = models.PositiveIntegerField()
    sale_price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()