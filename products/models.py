from django.db import models

from categories.models import Category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sold = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    on_sale = models.BooleanField(default=False)
    price = models.PositiveIntegerField()
    sale_price = models.PositiveIntegerField()
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=100, default='default_color')
    
    def __str__(self) -> str:
        return f'#{self.id} {self.product.name} {self.color} {self.size}'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='images/product/%Y/%m/%D/', blank=True, null=True)
    desc = models.CharField(max_length=200, default='', blank=True)

    def __str__(self) -> str:
        return f'{self.product.name} #{self.order}'
