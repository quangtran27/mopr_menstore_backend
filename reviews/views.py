from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from users.models import User

from .models import Review, ReviewImage
from .serializers import ReviewImageSerialzier, ReviewSerializer


@api_view(['POST'])
def add_review(request):
    user_id = request.POST.get('user_id')
    product_id = request.POST.get('product_id')
    star = (int)(request.POST.get('star'))
    desc = request.POST.get('desc')
    images = request.FILES.getlist('images')
    if (user_id is not None) and (product_id is not None) and (desc is not None) and (images is not None) and (star is not None and star > 1 and star <= 5):

        try:
            user = User.objects.get(pk=user_id)
            product = Product.objects.get(pk=product_id)
            review = Review(user=user, product=product, star=star, desc=desc)
            review.save()
            for image in images:
                review_image = ReviewImage(review=review, image=image)
                review_image.save()
            serializer = ReviewSerializer(review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except User.DoesNotExist or Product.DoesNotExist:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_review(request, review_id):
    try:
        review = Review.objects.get(pk=review_id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status.HTTP_200_OK)
    except Review.DoesNotExist:
        return Response({}, status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_review_images(request, review_id):
    try:
        review = Review.objects.get(pk=review_id)
        review_images = review.reviewimage_set.all()
        serializer = ReviewImageSerialzier(review_images, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    except Review.DoesNotExist:
        return Response({}, status.HTTP_404_NOT_FOUND)
