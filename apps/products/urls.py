from django.urls import path

from apps.products.api_endpoints.products.ProductList.views import product_list
from apps.products.views import get_products


urlpatterns = [
    path('products/', product_list, name='product_list'),
]
