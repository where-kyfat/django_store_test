import requests
from django.conf import settings
from django.db import transaction
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import OrderModel
from .serializers import OrderSerializer


@receiver(pre_save, sender=OrderModel)
def sync_store_order_pre(sender, instance, **kwargs):
    instance.start_trans = transaction.savepoint()


@receiver(post_save, sender=OrderModel)
def sync_store_create_update_post(sender, instance, created, **kwargs):
    if not created:
        try:
            endpoint_url = settings.STORE_ENDPOINT
            endpoint_data = OrderSerializer(instance).data
            response = requests.put(f'{endpoint_url}{instance.pk}/', endpoint_data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            transaction.savepoint_rollback(instance.start_trans)
            raise e
