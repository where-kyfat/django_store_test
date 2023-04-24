from django.urls import path
from .views import CreateOrderModel

urlpatterns = [
    path('', CreateOrderModel.as_view(), name='create-order'),
]
