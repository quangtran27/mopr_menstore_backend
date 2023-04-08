from rest_framework import serializers

from .models import Review, ReviewImage


class ReviewSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = [
            'id', 
            'user',
            'created', 
            'star', 
            'desc', 
            'images'
        ]
        depth = 0

    def get_images(self, obj):
        return [image.image.url for image in obj.reviewimage_set.all()]
    
class AddReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'user', 
            'phone',
            'created', 
            'star', 
            'desc',
        ]