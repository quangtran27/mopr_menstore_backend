from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import ProductDetail
from users.models import User

from .models import Cart, CartItem
from .serializers import CartSerializer


@api_view(['POST'])
def add_to_cart(request):
    '''Add item to cart'''
    success = False
    message = ''
    try:
        user_id = request.POST.get('user_id')
        product_detail_id = request.POST.get('product_detail_id')
        quantity = request.POST.get('quantity', 1)

        if quantity <= 0: 
            user = User.objects.get(id=user_id)
            product_detail = ProductDetail.objects.get(id=product_detail_id)

            # Check if cart exists for this user
            cart, _ = Cart.objects.get_or_create(user=user)

            # Check if cart item already exists for this product detail
            cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product_detail=product_detail)

            # Update quantity if item already exists
            if not item_created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity

            cart_item.save()
            message = 'Thêm sản phẩm vào giỏ hàng thành công'
        else:
            message = 'Số lượng không hợp lệ!\nThêm không thành công'
            success = True
    except Exception as e:
        message = 'Đã có lỗi xảy ra!\nThêm không thành công'
        print(e)

    return Response({
        'success': success,
        'message': message
    })

@api_view(['GET'])
def get_cart_by_user(request, phone):
    success = False
    serializer = None
    try:
        user = User.objects.get(phone=phone)
        carts = Cart.objects.filter(user=user)
        print(carts)
        serializer = CartSerializer(carts, many=True)
        success = True
    except Exception as e:
        print(e)

    return Response({
        'success': success,
        'data': serializer.data if serializer else []
    })

@api_view(['POST'])
def update_cart(request):
    success = False
    message = ''

    try:
        cart_item_id = (int)(request.POST.get('cart_item_id'))
        action = request.POST.get('action') # increase, decrease, delete
        
        cart_item = CartItem.objects.get(pk=cart_item_id)
        if action == 'increase':
            cart_item.quantity = cart_item.quantity + 1
            cart_item.save()
        elif action == 'decrease':
            cart_item.quantity = cart_item.quantity - 1
            cart_item.save()
        elif action == 'delete':
            cart_item.delete()

        message = 'Cập nhật thành công'
        success = True

    except Exception as e:
        print(e)
        message = 'Đã xảy ra lỗi!\nCập nhật không thành công'
    return Response({
        'success': success,
        'message': message,
    })