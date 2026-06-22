from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from apps.products.api_endpoints.products.ProductList.serializers import ProductListSerializer
from apps.products.api_endpoints.products.filters import ProductFilter
from apps.products.models import Product
from apps.products.pagination import CustomLimitOffsetPagination


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
