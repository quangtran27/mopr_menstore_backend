from django.db.models import Max, Q, Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category, Product, ProductDetail
from .serializers import CategorySerializer, ProductSerializer


@api_view(['GET'])
def get_all_categories(request):
    success = False
    serializer = None
    try:
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        success = True
    except:
        pass
    return Response({
			'success': success,
			'data': serializer.data if serializer else []
		})

@api_view(['GET'])
def get_top_sale_products(request):
    '''Get 8 best selling products'''
    success = False
    serializer = None
    try:
        top_products = Product.objects.filter(productdetail__sold__gt=0).annotate(total_sold=Sum('productdetail__sold')).order_by('-total_sold')[:6]
        serializer = ProductSerializer(top_products, many=True)
        success = True
    except Exception as e:
        print(e)
    return Response({
			'success': success,
			'data': serializer.data if serializer else []
		})

@api_view(['GET'])
def get_latest_products(request):
    '''Get 8 latest products'''
    success = False
    serializer = None
    try:
        latest_products = Product.objects.order_by('-id')[:8]
        serializer = ProductSerializer(latest_products, many=True)
        success = True
    except Exception as e:
        print(e)
    return Response({
        'success': success,
        'data': serializer.data if serializer else []
    })

@api_view(['GET'])
def search_products(request):
    success = True
    serializer = None
    try:
        keyword = request.GET.get('keyword', '')
        sort_by = request.GET.get('sort_by', 'price')
        order = request.GET.get('order', 'asc')
        category_id = (int) (request.GET.get('category_id', '0'))
        min_price = (int) (request.GET.get('min_price', '0'))
        max_price = (int) (request.GET.get('max_price', '99999999'))
        review = (int) (request.GET.get('review', '0'))

        # Filter products by keyword
        products = Product.objects.filter(Q(name__icontains=keyword) | Q(desc__icontains=keyword))

        # Filter products by category
        if category_id != 0:
            products = products.filter(category_id=category_id)

        # Filter products by price range
        products = products.filter(productdetail__price__gte=min_price, productdetail__price__lte=max_price)

        # Filter products by review
        if review != 0:
            products = products.filter(review__star=review)

        # Sort products
        if sort_by == 'price':
            products = products.order_by('productdetail__price')
        elif sort_by == 'created':
            products = products.order_by('-id')
        elif sort_by == 'sales':
            products = products.annotate(total_sold=Sum('productdetail__sold')).order_by('-total_sold')

        # Reverse order if necessary
        if order == 'desc':
            products = products.reverse()
            
        # Remove duplicates
        products = products.distinct()

        serializer = ProductSerializer(products, many=True)
    except Exception as e:
        print(e)
        success = False

    # Return response
    return Response({
        'success': success,
        'data': serializer.data if serializer else []
    })

@api_view(['GET'])
def get_product(request, product_id):
    success = False
    serializer = None
    selected = 0
    try:
        products = Product.objects.filter(id=product_id)

        _selected = products[0].productdetail_set.all()[0].id
        selected = request.GET.get('selected', _selected)
        
        # Check if selected item existed?
        selected_detail = ProductDetail.objects.filter(pk=selected)
        if not selected_detail.exists():
            selected = _selected

        serializer = ProductSerializer(products, many= True)
        success = True
    except Product.DoesNotExist:
        print(f'Sản phẩm có id {product_id} không tồn tại')
    except Exception as e:
        print(e)

    return Response({
            'success': success,
            'data': serializer.data if serializer else [],
            'selected': selected
        })