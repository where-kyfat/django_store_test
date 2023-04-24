from rest_framework.generics import CreateAPIView

from .models import OrderModel
from .serializers import OrderSerializer


class CreateOrderModel(CreateAPIView):
    """
    View for creating an order by warehouse
    """
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
