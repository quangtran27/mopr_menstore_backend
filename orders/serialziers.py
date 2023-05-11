from rest_framework import serializers

from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'user_id',
            'created',
            'updated',
            'status',
            'name',
            'phone',
            'address',
            'payment',
            'shipping_fee',
            'is_paid',
            'is_reviewed',
            'note',
            'total',
        ]

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            'id',
            'order_id',
            'product_detail_id',
            'on_sale',
            'price',
            'sale_price',
            'quantity',
        ]