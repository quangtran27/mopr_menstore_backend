from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category, Product, ProductDetail
from .serializers import CategorySerializer, ProductSerializer


@api_view(['GET'])
def get_all_categories(request):
    success = True
    serializer = { 'data': None }
    try:
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        pass
    except:
        success = False
    return Response({
			'success': success,
			'data': serializer.data if serializer else []
		})

# Products
@api_view(['GET'])
def get_all_products(request):
    success = True
    serializer = { 'data': None }
    try:
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        pass
    except:
        success = False
    return Response({
			'success': success,
			'data': serializer.data if serializer else []
		})

@api_view(['GET'])
def get_product(request, product_id):
    success = True
    serializer = { 'data': None }

    try:
        product = Product.objects.get(pk=product_id)

        _selected = product.details.all()[0].id
        selected = request.GET.get('selected', _selected)
        
        # Check if selected item existed?
        selected_detail = ProductDetail.objects.filter(pk=selected)
        if not selected_detail.exists():
            selected = _selected

        serializer = ProductSerializer(product)
        pass
    except Product.DoesNotExist:
        success = False

    try:
        _data = serializer.data
        _data['selected'] = (int) (selected)
    except:
        _data = serializer['data']

    return Response({
            'success': success,
            'data': _data
        })

# Define post methods for admin page here