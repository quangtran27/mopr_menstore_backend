from django.db import models

from products.models import ProductDetail
from users.models import User

ORDER_STATUS = ((1, 'Chờ xác nhận'), (2, 'Đang chuẩn bị hàng'), (3, 'Đang giao hàng'), (4, 'Đã giao'), (5, 'Đã hủy'))
ORDER_PAYMENT = ((1, 'COD'), (2, 'Chuyển khoản ngân hàng'), (3, 'Khác'))

class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    status = models.IntegerField(choices=ORDER_STATUS)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    payment = models.IntegerField(choices=ORDER_PAYMENT)
    is_paid = models.BooleanField(default=False)
    note = models.TextField()
    total = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'{self.created} {self.phone}'

class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product_detail = models.ForeignKey(to=ProductDetail, on_delete=models.PROTECT)
    on_sale = models.BooleanField(default=False)
    price = models.PositiveIntegerField()
    sale_price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()