from django.db import models

from products.models import Product
from users.models import User

STAR_CHOICES = ((1, '1 sao'), (2, '2 sao'), (3, '3 sao'), (4, '4 sao'), (5, '5 sao'))

class Review(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(to=Product, null=True)
    created = models.DateField(auto_now_add=True)
    star = models.IntegerField(choices=STAR_CHOICES, default=5)
    desc = models.TextField()

class ReviewImage(models.Model):
    review = models.ForeignKey(to=Review, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/review/%Y/%m/%D/', blank=True, null=True)