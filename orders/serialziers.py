from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
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
        ]