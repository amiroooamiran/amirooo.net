from django.contrib import admin
from .models import *
# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage

class ProductTypeInline(admin.TabularInline): 
    model = ProductType

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductTypeInline]

admin.site.register(Product, ProductAdmin)