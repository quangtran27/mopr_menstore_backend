from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            'id',
            'product_detail',
            'on_sale',
            'price',
            'sale_price',
            'quantity',
        ]
        depth = 1

class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'created',
            'updated',
            'status',
            'name',
            'phone',
            'address',
            'payment',
            'is_paid',
            'note',
            'total',
            'order_items',
        ]

    def get_order_items(self, obj):
        _order_items = obj.orderitem_set.all()
        serializer = OrderItemSerializer(_order_items, many=True)
        return serializer.data
