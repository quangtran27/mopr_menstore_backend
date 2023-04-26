from rest_framework import serializers

from .models import Review, ReviewImage


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id', 
            'user_id',
            'product_id',
            'created', 
            'star', 
            'desc', 
        ]

class ReviewImageSerialzier(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = [
            'id',
            'review_id',
            'image',
        ]