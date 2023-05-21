from rest_framework import serializers

from .models import Cart, CartItem


class CartSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = ( 'id', 'user_id', )
    def get_user_id(self, obj):
        return obj.user.id


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ( 'id', 'cart_id', 'product_detail_id', 'quantity', )
