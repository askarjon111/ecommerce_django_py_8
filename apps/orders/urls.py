from django.urls import path

from apps.orders.api_endpoints.orders.OrderCreate.views import OrderCreateAPIView
from apps.orders.api_endpoints.orders.OrderDetail.views import OrderDetailAPIView
from apps.orders.api_endpoints.orders.OrderList.views import OrderListAPIView
from apps.orders.api_endpoints.orders.OrderUpdateDestroy.views import order_update_destroy_view


urlpatterns = [
    path('', OrderListAPIView.as_view(), name='order-list'),
    path('create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('<int:pk>/', OrderDetailAPIView.as_view(), name='order-detail'),
    path('<int:pk>/update/', order_update_destroy_view, name='order-update'),
    path('<int:pk>/delete/', order_update_destroy_view, name='order-delete'),
]
