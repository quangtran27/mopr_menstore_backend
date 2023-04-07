from django.contrib import admin
from nested_inline.admin import NestedModelAdmin, NestedStackedInline

from .models import Category, Product, ProductDetail, ProductImage


class ProductDetailInline(NestedStackedInline):
    model = ProductDetail
    extra = 0
    fk_name = 'product'

class ProductImageInline(NestedStackedInline):
    model = ProductImage
    extra = 0
    fk_name = 'product'

class ProductAdmin(NestedModelAdmin):
    model = Product
    inlines = [ProductDetailInline, ProductImageInline]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductDetail)