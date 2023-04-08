from django.contrib import admin
from nested_inline.admin import NestedModelAdmin, NestedStackedInline

from .models import Review, ReviewImage


class ReviewImageInline(NestedStackedInline):
    model = ReviewImage
    extra = 0
    fk_name = 'review'

class ReviewAdmin(NestedModelAdmin):
    model = Review
    inlines = [ReviewImageInline]

admin.site.register(Review, ReviewAdmin)