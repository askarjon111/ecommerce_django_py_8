from django.urls import path

from apps.orders.api_endpoints.orders.OrderCreate.views import order_create_view
from apps.orders.api_endpoints.orders.OrderList.views import order_list_view


urlpatterns = [
    path('', order_list_view, name='order-list'),
    path('create/', order_create_view, name='order-create'),
]
