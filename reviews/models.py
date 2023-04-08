from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from products.models import Product
from users.models import User


class Review(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    star = models.IntegerField(
        validators=[
            MaxValueValidator(5, message='Value must be between 1 and 5'),
            MinValueValidator(1, message='Value must be between 1 and 5')
        ]
    )
    desc = models.TextField()

class ReviewImage(models.Model):
    review = models.ForeignKey(to=Review, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/review/%Y/%m/%D/', blank=True, null=True)