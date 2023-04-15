from django.contrib import admin
from nested_inline.admin import NestedModelAdmin, NestedStackedInline

from .models import Order, OrderItem


class OrderItemInline(NestedStackedInline):
    model = OrderItem
    extra = 0
    fk_name = 'order'

class OrderAdmin(NestedModelAdmin):
    model = Order
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)