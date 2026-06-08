from django.shortcuts import render

from apps.products.models import *


def home(request):
    catigories = Catigory.objects.all()
    products = Product.objects.all()
    
    data = {
        'catigories': catigories,
        'products': products
    }
    return render(request, 'common/home.html',data)
