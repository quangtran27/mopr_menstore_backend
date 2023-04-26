from django.core.paginator import Paginator
from django.db.models import Max, Min, Q, Sum
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from reviews.serializers import ReviewSerializer

from .models import Category, Product, ProductDetail
from .serializers import (
    ProductDetailSerializer,
    ProductImageSerializer,
    ProductSerializer,
)

PRODUCTS_PER_PAGE = 12


@api_view(['GET'])
def get_all_products(request):
    page = (int) (request.GET.get('page', '1'))
    sort_by = request.GET.get('sort_by', '')
    order = request.GET.get('order', 'asc')

    products = Product.objects.all()
    
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

    # Paging
    paginator = Paginator(products, PRODUCTS_PER_PAGE)
    if page > paginator.num_pages or page < 1: page = 1
    paginated_products = paginator.page(page)

    serializer = ProductSerializer(paginated_products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_top_sale_products(request):
    '''Get 8 best selling products'''
    top_products = Product.objects.filter(productdetail__sold__gt=0).annotate(total_sold=Sum('productdetail__sold')).order_by('-total_sold')[:6]
    serializer = ProductSerializer(top_products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_latest_products(request):
    '''Get 8 latest products'''
    latest_products = Product.objects.order_by('-id')[:8]
    serializer = ProductSerializer(latest_products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK) 

@api_view(['GET'])
def search_products(request):
    keyword = request.GET.get('keyword', '')
    page = (int) (request.GET.get('page', '1'))
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

    # Paging
    paginator = Paginator(products, PRODUCTS_PER_PAGE)
    if page > paginator.num_pages or page < 1: page = 1
    paginated_products = paginator.page(page)

    serializer = ProductSerializer(paginated_products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_product_details(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        product_details = product.productdetail_set.all()
        serializer = ProductDetailSerializer(product_details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_product_detail(request, product_detail_id):
    try:
        product_detail = ProductDetail.objects.get(pk=product_detail_id)
        serializer = ProductDetailSerializer(product_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    
@api_view(['GET'])
def get_product_images(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        product_images = product.productimage_set.all()
        serializer = ProductImageSerializer(product_images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_product_reviews(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        product_reviews = product.review_set.all()
        serializer = ReviewSerializer(product_reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)