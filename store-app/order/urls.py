from django.urls import path

from .views import UpdateOrderModel

urlpatterns = [
    path('<str:pk>/', UpdateOrderModel.as_view(), name='order-detail'),
]
