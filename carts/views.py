from django.http import HttpRequest, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import ProductDetail
from users.models import User

from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer


@api_view(['GET'])
def get_cart(request, cart_id):
    try:
        cart = Cart.objects.get(pk=cart_id)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Cart.DoesNotExist as e:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def get_or_add_cart_items(request, cart_id: int):
    try:
        cart = Cart.objects.get(pk=cart_id)
    except Cart.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET': # get cart items
        cart_items = cart.cartitem_set.all()
        serialzier = CartItemSerializer(cart_items, many=True)
        return Response(serialzier.data, status=status.HTTP_200_OK)
    elif request.method == 'POST': # add cart item
        product_detail_id = (int) (request.POST.get('product_detail_id', '0'))
        quantity = (int) (request.POST.get('quantity', '1'))
        if quantity <= 0:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product_detail = ProductDetail.objects.get(id=product_detail_id)
        except ProductDetail.DoesNotExist:
            return Response({}, status.HTTP_404_NOT_FOUND)

        # Check if cart item already exists for this product detail
        cart_item, is_created = CartItem.objects.get_or_create(cart=cart, product_detail=product_detail)

        if is_created: # Cart item doesn't exist
            if quantity <= product_detail.quantity:
                cart_item.quantity = quantity
            else: return Response({}, status=status.HTTP_400_BAD_REQUEST)
        else: # Cart item already exists
            if cart_item.quantity + quantity <= product_detail.quantity:
                cart_item.quantity += quantity
            else: return Response({}, status=status.HTTP_400_BAD_REQUEST)
        cart_item.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['PUT', 'DELETE'])
def update_or_delete_cart_item(request, cart_id: int, cart_item_id: int):
    try:
        cart = Cart.objects.get(id=cart_id)
        cart_item = CartItem.objects.get(id=cart_item_id)
    except (Cart.DoesNotExist, CartItem.DoesNotExist):
        return Response({}, status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT': # update cart item
        try:
            quantity = (int) (request.POST.get('quantity'))
        except ValueError as e:
            print(e)
            return Response({}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        if (quantity <= 0) or (quantity > cart_item.product_detail.quantity):
            return Response({}, status.HTTP_400_BAD_REQUEST)
        
        cart_item.quantity = quantity
        cart_item.save()
        return Response(CartItemSerializer(cart_item).data, status=status.HTTP_200_OK)
    else: # delete cart item
        cart_item.delete()
        return Response({}, status=status.HTTP_200_OK)