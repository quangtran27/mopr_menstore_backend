from distutils.command import upload
from turtle import update

from django.db import models


class Banner(models.Model):
	order = models.IntegerField()
	image = models.ImageField(upload_to='images/banners/%Y/%m/%D/')
	def __str__(self) -> str:
		return f'Banner #{self.order}'
