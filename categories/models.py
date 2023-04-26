from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/category/%Y/%m/%D/', blank=True, null=True)

    def __str__(self) -> str:
        return self.name