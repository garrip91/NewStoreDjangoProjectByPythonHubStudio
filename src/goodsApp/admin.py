from django.contrib import admin
from .models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    
    pass


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    
    pass
