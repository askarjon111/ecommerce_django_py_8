from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

from apps.products.api_endpoints.products.ProductList.serializers import ProductListSerializer
from apps.products.models import Product
from apps.products.pagination import CustomLimitOffsetPagination


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = CustomLimitOffsetPagination
