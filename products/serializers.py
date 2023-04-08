from rest_framework import serializers

from .models import Category, Product, ProductDetail


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'desc', 'image')

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = [
            'id', 
            'product', 
            'sold', 
            'quantity', 
            'on_sale',
            'price',
            'sale_price',
            'size',
            'color',
        ]

class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    details = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'desc', 'status', 'details', 'images')
        depth = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].validators = []

    def get_details(self, obj):
        product_details = obj.productdetail_set.all()
        serializer = ProductDetailSerializer(product_details, many=True)
        return serializer.data
    
    def get_images(self, obj):
        return [ { 'order': image.order, 'url': image.image.url, 'desc': image.desc,  } for image in obj.productimage_set.all() ]
    