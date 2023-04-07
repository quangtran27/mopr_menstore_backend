from rest_framework import serializers

from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            'id',
            'product_detail',
            'quantity',
        ]
        depth = 1

class CartSerializer(serializers.ModelSerializer):
    cart_items = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'cart_items']

    def get_cart_items(self, obj):
        _cart_items = obj.cartitem_set.all()
        serializer = CartItemSerializer(_cart_items, many=True)
        return serializer.data
