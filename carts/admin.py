from django.contrib import admin
from nested_inline.admin import NestedModelAdmin, NestedStackedInline

from .models import Cart, CartItem


class CartItemInline(NestedStackedInline):
    model = CartItem
    extra = 0
    fk_name = 'cart'

class CartAdmin(NestedModelAdmin):
    model = Cart
    inlines = [CartItemInline]

admin.site.register(Cart, CartAdmin)