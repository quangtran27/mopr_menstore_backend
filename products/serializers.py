from rest_framework import serializers

from .models import Product, ProductDetail, ProductImage


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ 
            'id', 
            'category_id',
            'name', 
            'desc', 
            'status', 
        ]
        
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = [
            'id', 
            'product_id', 
            'sold', 
            'quantity', 
            'on_sale',
            'price',
            'sale_price',
            'size',
            'color',
        ]

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = [
            'id',
            'product_id',
            'order',
            'image',
            'desc',
        ]