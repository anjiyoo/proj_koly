from django.contrib import admin
from seller.models import Category, Products

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id', 'name')


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display=('user', 'category', 'name', 'price', 'description', 'image_url')
