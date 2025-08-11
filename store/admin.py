from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'mrp', 'rating', 'category', 'created_at')
    list_filter = ('category', 'rating', 'created_at')
    search_fields = ('category__name',)

