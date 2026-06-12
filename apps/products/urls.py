from django.urls import path

from apps.products.api_endpoints.products.ProductList.views import product_list
from apps.products.api_endpoints.products.ProductDetail.views import product_detail
from apps.products.api_endpoints.products.ProductCreate.views import product_create
from apps.products.api_endpoints.products.ProductUpdateDestroy.views import product_update,product_destroy


urlpatterns = [
    path('', product_list, name='product_list'),
    path('<int:pk>/', product_detail, name='product_detail'),
    path('create/', product_create, name='product_create'),
    path('<int:pk>/update/', product_update, name='product_update'),
    path('<int:pk>/delete/', product_destroy, name='product_delete'),
]
