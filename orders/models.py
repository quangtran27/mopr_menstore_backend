from django.db import models

from products.models import Product

ORDER_STATUS = ((1, 'Created'), (2, 'Delivering'), (3, 'Delivered'), (4, 'Cancelled'))
ORDER_PAYMENT = ((1, 'COD'), (2, 'Banking'), (3, 'Others'))

class Order(models.Model):
    name = models.CharField(max_length=200, default='Customer Name')
    customer_phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    delivered = models.DateTimeField()
    is_paid = models.BooleanField(default=False)
    status = models.IntegerField(choices=ORDER_STATUS)
    payment = models.IntegerField(choices=ORDER_PAYMENT)
    note = models.TextField()
    total = models.PositiveIntegerField()

class OrderItem(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.PROTECT)
    on_sale = models.BooleanField(default=False)
    price = models.PositiveIntegerField()
    sale_price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()