from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'desc', 'image')

class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('name', 'desc', 'status', 'details', 'images')
        depth = 1
    
    def get_images(self, obj):
        return [ { 'order': image.order, 'url': image.image.url, 'desc': image.desc,  } for image in obj.productimage_set.all() ]