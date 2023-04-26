from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer


@api_view(['GET'])
def get_all_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_category(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
        serialzier = CategorySerializer(category)
        return Response(serialzier.data, status.HTTP_200_OK)
    except Category.DoesNotExist:
        return Response({}, status.HTTP_404_NOT_FOUND)
    