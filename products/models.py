from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/category/%Y/%m/%D/', blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='Product name')
    desc = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

class ProductDetail(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='details')
    sold = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    on_sale = models.BooleanField(default=False)
    price = models.PositiveIntegerField()
    sale_price = models.PositiveIntegerField()
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=100, default='default_color')

class ProductImage(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='images/product/%Y/%m/%D/', blank=True, null=True)
    desc = models.CharField(max_length=200, default='')
