from django.shortcuts import render

from apps.products.models import Product

def get_products(request):
    products = Product.objects.all()
    print(products)
    return render(request,'products/list.html',{'products': products})
