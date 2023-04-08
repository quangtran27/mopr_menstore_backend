from rest_framework.decorators import api_view
from rest_framework.response import Response

from carts.models import CartItem
from products.models import ProductDetail
from users.models import User

from .models import Order, OrderItem
from .serialziers import OrderSerializer


@api_view(['POST'])
def add_order(request):
    success = False
    message = ''
    order = None

    try:
        user_phone = request.POST.get('user_phone')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        payment = request.POST.get('payment')
        note = request.POST.get('note')
        cart_item_ids = request.POST.get('cart_item_ids').split(':')

        status = 1
        is_paid = False
        total = 0

        order = Order(
            user=User.objects.get(phone=user_phone),
            status=status,
            name=name,
            phone=phone,
            address=address,
            payment=payment,
            is_paid=is_paid,
            note=note,
            total=total,
        )
        order.save()

        # Check if any order items has invalid quantity
        for cart_item_id in cart_item_ids:
            cart_item = CartItem.objects.get(pk=cart_item_id)
            product_detail = cart_item.product_detail
            if cart_item.quantity > product_detail.quantity:
                if order is not None:
                    order.delete()
                return Response({
                    'success': False, 
                    'message': 'Số lượng không hợp lệ!\nĐặt hàng không thành công'
                })
            
        for cart_item_id in cart_item_ids:
            cart_item = CartItem.objects.get(pk=cart_item_id)
            product_detail = cart_item.product_detail
            order_item = OrderItem(
                order=order,
                product_detail=product_detail,
                on_sale=product_detail.on_sale,
                price=product_detail.price,
                sale_price=product_detail.sale_price,
                quantity=cart_item.quantity,
            )
            order_item.save()

            product_detail.quantity -= order_item.quantity
            product_detail.sold += order_item.quantity
            product_detail.save()

            order.total += (order_item.sale_price if order_item.on_sale else order_item.price) * order_item.quantity
            order.save()
            cart_item.delete()
        message = 'Đặt hàng thành công'
        success = True

    except Exception as e:
        print(e)
        if order is not None:
            order.delete()
        message = 'Đã xảy ra lỗi!\nĐặt hàng không thành công'

    return Response({
        'success': success, 
        'message': message}
    )
    

@api_view(['GET'])
def get_order(request, order_id):
    success = False
    serializer = None
    
    try:
        orders = Order.objects.filter(id=order_id)
        serializer = OrderSerializer(orders, many=True)
        success = True
    except Exception as e:
        print(e)
    
    return Response({
        'success': success,
        'data': serializer.data if serializer else []
    })

@api_view(['GET'])
def get_orders_by_user(request, phone):
    success = False
    serializer = None
    
    try:
        user = User.objects.get(phone=phone)
        orders = user.order_set.all()
        serializer = OrderSerializer(orders, many=True)
        success = True
    except Exception as e:
        print(e)
    
    return Response({
        'success': success,
        'data': serializer.data if serializer else []
    })

@api_view(['POST'])
def update_order(request):
    success = False
    message = ''

    try:
        order_id = request.POST.get('order_id')
        status = request.POST.get('status')
        is_paid = request.POST.get('is_paid')
        order = Order.objects.get(pk=order_id)
        if status is not None:
            order.status = status
        if is_paid is not None:
            order.is_paid = is_paid
        order.save()
        success = True
        message = 'Cập nhật thành công'

    except Order.DoesNotExist:
        message = 'Cập nhật không thành công!\nĐơn hàng không tồn tại'
    except Exception as e:
        print(e)
        message = 'Cập nhật không thành công!\nĐã xảy ra lỗi'

    return Response({
        'success': success, 
        'message': message
    })
