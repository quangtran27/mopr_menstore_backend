from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from users.models import User

from .models import Review, ReviewImage
from .serializers import AddReviewSerializer, ReviewSerializer

SPLITTER = '<>'


@api_view(['GET'])
def get_reviews_by_product(request, product_id):
    success = False
    serializer = None

    try:
        reviews = Review.objects.filter(product_id=product_id)
        serializer = ReviewSerializer(reviews, many=True)
        success = True
    except:
        pass

    return Response({
        'success': success,
        'data': serializer.data if serializer else []
    })

@api_view(['POST'])
def add_review(request):
    success = False
    message = ''
    try:
        phone = request.POST.get('phone')
        product_id = request.POST.get('product_id')
        star = (int)(request.POST.get('star'))
        desc = request.POST.get('desc')
        images = request.FILES.getlist('images')

        if phone and product_id and (desc is not None) and (images is not None):
            user = User.objects.get(phone=phone)
            product = Product.objects.get(pk=product_id)

            review = Review(user=user, product=product, star=star, desc=desc)
            review.save()
            for image in images:
                review_image = ReviewImage(review=review, image=image)
                review_image.save()
            message = 'Đánh giá thành công!'
            success = True
        else:
            message = 'Đánh giá không thành công!\nThông tin không hợp lệ'
    except Exception as e:
        print(e)
        message = 'Đánh giá không thành công!\nĐã có lỗi xảy ra'
    
    return Response({
            'success': success,
            'message': message
        })
