from django.shortcuts import render
from .models import Product

def product_list(request):
    # Fetch all active footwear from the database
    products = Product.objects.filter(is_active=True)
    return render(request, 'shop/product_list.html', {'products': products})
