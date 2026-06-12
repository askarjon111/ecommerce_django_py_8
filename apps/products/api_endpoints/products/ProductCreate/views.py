from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from apps.products.api_endpoints.products.ProductCreate.serializers import ProductCreateSerializer
from apps.products.models import Product

@extend_schema(request=ProductCreateSerializer)
@api_view(['POST'])
def product_create(request):
    serializer = ProductCreateSerializer(request.data)
    if serializer.is_valid():
        product=serializer.save()
        return Response(ProductCreateSerializer(product).data,status=201)
    return Response(serializer.errors,status=400)
