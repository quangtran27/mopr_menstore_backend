from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserLoginSerializer, UserSerializer


@api_view(['POST'])
def register(request):
    success = False
    message = ''
    try:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            success = True
            serializer.save()
            message = 'Đăng ký thành công!'
        else:
            message = 'Đăng ký không thành công!\nThông tin không hợp lệ'
    except:
        message = 'Đăng ký không thành công!\nĐã có lỗi xảy ra'
    
    return Response({
            'success': success,
            'message': message
        })

@api_view(['POST'])
def login(request):
    success = False
    message = ''
    try:
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.filter(phone=serializer.validated_data['phone'], password=serializer.validated_data['password']).first()
            if user:
                success = True
                message = 'Đăng nhập thành công!'
            else:
                message = 'Đăng nhập không thành công!\nTài khoản hoặc mật khẩu chưa chính xác'
            
        else:
            message = 'Đăng nhập không thành công!\nThông tin không hợp lệ'
    except:
        message = 'Đăng nhập không thành công!\nĐã có lỗi xảy ra'
    
    return Response({
            'success': success,
            'message': message
        })

@api_view(['POST'])
def change_password(request):
    success = False
    message = ''
    try:
        phone = request.POST.get('phone')
        old_password = request.POST.get('old-password')
        new_password = request.POST.get('new-password')
        if old_password != new_password:
            user = User.objects.filter(phone=phone, password=old_password).first()
            if user:
                user.password = new_password
                user.save()
                success = True
                message = 'Thay đổi mật khẩu thành công'
            else:
                message = 'Mật khẩu chưa chính xác'
        else:
            message = 'Mật khẩu mới không được trùng với mật khẩu hiện tại'
    except:
        message = 'Thay đổi mật khẩu không thành công!\nĐã có lỗi xảy ra'

    return Response({
            'success': success,
            'message': message
        })

@api_view(['GET'])
def get_user(request, phone):
	success= False
	serializer = None

	try: 
		user = User.objects.filter(phone=phone)
		serializer = UserSerializer(user, many=True)
		success = True
	except:
		pass

	return Response({
		'success': success,
		'data': serializer.data if serializer else []
	})

@api_view(['POST'])
def update_user(request):
    success = False
    message = ''
    try:
        # Get parameters from request
        phone = request.POST.get('phone')
        name = request.POST.get('name')
        address = request.POST.get('address')
        birthday = request.POST.get('birthday')
        email = request.POST.get('email')
        image = request.FILES.get('image')

        # Check if user exists
        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            return Response({
                'success': False, 
                'message': 'Người dùng không tồn tại'
            })

        # Update user data
        user.name = name
        if image:
            user.image = image
        user.address = address
        user.birthday = birthday
        user.email = email
        user.save()

        success = True
        message = 'Cập nhật thành công'

    except Exception as e:
        print(e)
        message = 'Đã xảy ra lỗi!\nCập nhật không thành công'
    
    return Response({
        'success': success,
        'message': message
    })
