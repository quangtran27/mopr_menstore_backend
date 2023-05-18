from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)
    birthday = models.DateField(default='2000-01-01') # YYYY-MM-DD
    gender = models.CharField(max_length=10, default='Nam')
    email = models.CharField(unique=True, blank=True, max_length=255)
    image = models.ImageField(upload_to='images/user/%Y/%m/%D/', blank=True, null=True)
    address = models.CharField(max_length=200, default='')
    is_staff = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.phone