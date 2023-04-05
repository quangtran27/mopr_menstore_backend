from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer


@api_view(['POST'])
def user_register(request):
    success = True
    serializer = { 'data': None }
    messages = []
    try:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            messages.append('Create successfully')
        else:
            success = False
            for field, errors in serializer.errors.items():
                messages.append(f"{field.capitalize()}: {', '.join(errors)}")
            serializer = { 'data': None }
    except:
        success = False
        messages.append('An error occurred while creating a new account')
    
    try:
        _data = serializer.data
    except:
        _data = None
    
    return Response({
            'success': success,
            'data': _data,
            'messages': messages
        })

@api_view(['POST'])
def user_login(request):
    pass

@api_view(['POST'])
def user_logout(request):
    pass
