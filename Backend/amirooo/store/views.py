from django.shortcuts import render
from .models import *
# Create your views here.

def store(request):
    products = Product.objects.all()
    productImages = ProductImage.objects.all()

    context = {
        products : 'products',
        productImages : 'productImages',
    }
    return render(request, 'store/store.html', context)

def product(request):
    return render(request, 'store/product.html')