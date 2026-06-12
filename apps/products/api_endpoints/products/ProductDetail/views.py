from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.products.api_endpoints.products.ProductDetail.serializers import ProductDetailSerializer
from apps.products.models import Product


@api_view(['GET'])
def product_detail(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductDetailSerializer(product)
    return Response(serializer.data)
