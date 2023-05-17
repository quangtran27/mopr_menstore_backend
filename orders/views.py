from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from carts.models import CartItem
from products.models import ProductDetail
from users.models import User

from .models import Order, OrderItem
from .serialziers import OrderItemSerializer, OrderSerializer


@api_view(['POST'])
def add_order(request):
    user_id = (int) (request.POST.get('user_id'))
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    payment = (int) (request.POST.get('payment'))
    cart_item_ids = request.POST.get('cart_item_ids')
    note = request.POST.get('note')

    ordrer_status = 1
    is_paid = False
    total = 0

    try:
        cart_item_ids = cart_item_ids.split(',')
        # Check payment method:
        if payment < 1 or payment > 3:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if any order items doesn't belong to user or cart has invalid quantity 
        for cart_item_id in cart_item_ids:
            cart_item = CartItem.objects.get(pk=cart_item_id)
            product_detail = cart_item.product_detail
            if cart_item.quantity > product_detail.quantity or cart_item.cart.user.id != user_id:
                return Response({}, status=status.HTTP_400_BAD_REQUEST)

        order = Order(
            user=User.objects.get(pk=user_id),
            status=ordrer_status,
            name=name,
            phone=phone,
            address=address,
            payment=payment,
            is_paid=is_paid,
            note=note,
            total=total,
        )
        order.save()

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

        serialzier = OrderSerializer(order)
        return Response(serialzier.data, status=status.HTTP_201_CREATED)
    except AttributeError as attr_err:
        print(attr_err)
        return Response({}, status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT'])
def get_or_update_order(request, order_id):
    if request.method == 'GET':
        try:
            orders = Order.objects.get(id=order_id)
            serializer = OrderSerializer(orders)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND) 
    elif request.method == 'PUT':
        order_status = request.POST.get('status')
        is_paid = request.POST.get('is_paid')
        is_reviewed = request.POST.get('is_reviewed')
        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        if order_status is not None:
            order.status = order_status
        if is_paid is not None:
            order.is_paid = is_paid
        if is_reviewed is not None: 
            order.is_reviewed = is_reviewed
        order.save()
        return Response({}, status=status.HTTP_200_OK)

    else: return Response({}, status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def get_order_items(request, order_id):
    try:
        order_items = OrderItem.objects.filter(order_id=order_id)
        serializer = OrderItemSerializer(order_items, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    except Order.DoesNotExist:
        return Response([], status=status.HTTP_404_NOT_FOUND)