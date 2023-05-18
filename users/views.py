from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from carts.models import Cart
from carts.serializers import CartSerializer
from notifications.models import Notification
from notifications.serializers import NotificationSerializer
from orders.serialziers import OrderSerializer
from users import serializers

from .models import User
from .serializers import UserLoginSerializer, UserSerializer


@api_view(['POST'])
def login(request):
    user_login_serializer = UserLoginSerializer(data=request.data)
    if user_login_serializer.is_valid():
        try:
            user = User.objects.get(phone=user_login_serializer.validated_data['phone'], password=user_login_serializer.validated_data['password'])
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def staff_login(request):
    user_login_serializer = UserLoginSerializer(data=request.data)
    if user_login_serializer.is_valid():
        try:
            user = User.objects.get(phone=user_login_serializer.validated_data['phone'], password=user_login_serializer.validated_data['password'], is_staff=True)
            return Response(UserSerializer(user).data, status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({}, status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({}, status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_201_CREATED)
    else:
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_user_info(request, user_id):
    try: 
        user = User.objects.get(pk=user_id)
        user.password = ''
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT'])
def get_or_update_user(request, user_id):
    if request.method == 'GET':
        try: 
            user = User.objects.get(pk=user_id)
            user.password = ''
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        name = request.POST.get('name')
        address = request.POST.get('address')
        birthday = request.POST.get('birthday')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        try:
            user = User.objects.get(id=user_id)
            user.name = name
            user.address = address
            user.birthday = birthday
            user.email = email
            if image:
                user.image = image
            user.save()
            return Response({}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def change_password(request, user_id):
    old_password = request.POST.get('old_password')
    new_password = request.POST.get('new_password')
    if (new_password is not None and len(new_password) >= 8) and (old_password != new_password):
        try:
            user = User.objects.get(pk=user_id, password=old_password)
            user.password = new_password
            user.save()
            return Response({}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND) 
    else:
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_user_orders(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        orders = user.orders.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_user_notifications(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        notifications = user.notification_set.all().order_by('-id')
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_user_cart(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        cart, _ = Cart.objects.get_or_create(user=user)
        print('cart: ',cart)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
