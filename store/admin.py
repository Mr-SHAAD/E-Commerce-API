from django.contrib import admin

from .models import Category, Product, Cart, CartItem, Order, OrderItem, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'category']
    search_fields = ['name']
    list_filter = ['category']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'total_price', 'created_at']
    list_filter = ['status']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating']

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(OrderItem)
# Register your models here.
