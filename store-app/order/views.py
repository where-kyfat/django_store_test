from rest_framework.generics import UpdateAPIView

from .models import OrderModel
from .serializers import OrderSerializer


class UpdateOrderModel(UpdateAPIView):
    """
    View for updating an order by warehouse
    """
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
