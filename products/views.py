from unicodedata import category

from django.core.paginator import EmptyPage, Paginator
from django.db.models import Avg, Case, Max, Min, Q, Sum, When
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from reviews.serializers import ReviewSerializer

from .models import Category, Product, ProductDetail
from .serializers import (
    ProductDetailSerializer,
    ProductImageSerializer,
    ProductSerializer,
    ProductSerializer2,
)

PAGE_SIZE = 12


@api_view(['GET'])
def get_all_products(request):
    page = request.GET.get('page')
    page_size = request.GET.get('page_size', PAGE_SIZE)
    name = request.GET.get('name')
    category_id = request.GET.get('categoryId', '0')
    min_price = request.GET.get('minPrice')
    max_price = request.GET.get('maxPrice')
    star = request.GET.get('star')
    sort_by = request.GET.get('sortBy', '')
    order = request.GET.get('order', 'asc')

    products = Product.objects.filter(status=True)

    # Filter
    if name is not None:
        products = products.filter(name__icontains=name)
    if (int) (category_id) > 0:
        products = products.filter(category__id=category_id)
    if min_price is not None and max_price is not None:
        try:
            min_price = (int) (min_price)
            max_price = (int) (max_price)
            products = products.filter(
                Q(productdetail__on_sale=False, productdetail__price__range=(min_price, max_price)) |
                Q(productdetail__on_sale=True, productdetail__sale_price__range=(min_price, max_price))
            ).distinct()
        except:
            products = []
    if star is not None:
        if (int) (star) > 0: 
            products = products.annotate(avg_star=Avg('review__star')).filter(avg_star__gte=star)
    
    # Sort
    if sort_by == 'price':
        products = products.annotate(
            min_price=Min('productdetail__price')
        ).order_by('min_price').distinct()
    elif sort_by == 'created':
        products = products.order_by('-id')
    elif sort_by == 'sales':
        products = products.annotate(total_sold=Sum('productdetail__sold')).order_by('-total_sold')
    if order == 'desc':
        products = products.reverse()
    
    # Paging
    if page is not None:
        page = (int) (page)
        page_size = (int) (page_size)
        paginator = Paginator(products, page_size)
        try:
            paginated_products = paginator.page(page)
        except EmptyPage:
            paginated_products = []
        return Response({
            'data': ProductSerializer(paginated_products, many=True).data,
            'pagination': {
                'page': page,
                'page_size': page_size,
                'total': paginator.count,
            }
        }, status.HTTP_200_OK)
    else:
        return Response(ProductSerializer(products, many=True).data, status=status.HTTP_200_OK)


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
    


@api_view(['GET'])
def get_all_products_api(request):
    page = request.GET.get('page')
    page_size = request.GET.get('page_size', PAGE_SIZE)
    name = request.GET.get('name')
    category_id = request.GET.get('category_id', '0')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    star = request.GET.get('star')
    sort_by = request.GET.get('sort_by', '')
    order = request.GET.get('order', 'asc')

    products = Product.objects.filter(status=True)

    # Filter
    if name is not None:
        products = products.filter(Q(name__icontains=name) | Q(desc__icontains=name))
    if (int) (category_id) > 0:
        products = products.filter(category__id=category_id)
    if min_price is not None:
        products = products.filter(productdetail__price__gte=min_price)
    if max_price is not None:
        products = products.filter(productdetail__price__lte=max_price)
    if star is not None:
        if (int) (star) > 0: 
            products = products.annotate(avg_star=Avg('review__star')).filter(avg_star__gte=star)
    
    # Sort
    if sort_by == 'price':
        products = products.order_by('productdetail__price').distinct()
    elif sort_by == 'created':
        products = products.order_by('-id')
    elif sort_by == 'sales':
        products = products.annotate(total_sold=Sum('productdetail__sold')).order_by('-total_sold')
    if order == 'desc':
        products = products.reverse()
    
    # Paging
    if page is not None:
        page = (int) (page)
        page_size = (int) (page_size)
        paginator = Paginator(products, page_size)
        try:
            paginated_products = paginator.page(page)
        except EmptyPage:
            paginated_products = []
        return Response({
            'data': ProductSerializer2(paginated_products, many=True).data,
            'pagination': {
                'page': page,
                'page_size': page_size,
                'total': paginator.count,
            }
        }, status.HTTP_200_OK)
    else:
        return Response(ProductSerializer2(products, many=True).data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_top_sales_products_api(request):
    '''Get 8 best selling products'''
    top_products = Product.objects.filter(productdetail__sold__gt=0).annotate(total_sold=Sum('productdetail__sold')).order_by('-total_sold')[:6]
    serializer = ProductSerializer2(top_products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)