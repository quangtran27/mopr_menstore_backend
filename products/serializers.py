from rest_framework import serializers

from .models import Product, ProductDetail, ProductImage


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ( 'id', 'category_id','name', 'desc', 'status' )

class ProductSerializer2(serializers.ModelSerializer):
    details = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ( 'id', 'category_id','name', 'desc', 'status','details','images' )   
    def get_details(self, obj):
        return [ ProductDetailSerializer(detail).data for detail in obj.productdetail_set.all() ]
    def get_images(self, obj):
        return [ image.image.url  for image in obj.productimage_set.all() ]

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = ( 'id',  'product_id',  'sold',  'quantity',  'on_sale', 'price', 'sale_price', 'size', 'color' )

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ( 'id','product_id','order','image','desc' )