from django.urls import path

from apps.products.views import get_products


urlpatterns = [
    path('products/', get_products, name='product_list'),
]
