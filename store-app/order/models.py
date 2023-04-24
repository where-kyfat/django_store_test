from django.db import models


class OrderModel(models.Model):
    name = models.CharField(max_length=25, primary_key=True)

    NEW = 'NE'
    IN_PROCESS = 'IP'
    STORED = 'ST'
    SEND = 'SE'
    STATUS_CHOICES = (
        (NEW, 'New'),
        (IN_PROCESS, 'In Process'),
        (STORED, 'Stored'),
        (SEND, 'Send')
    )

    status = models.CharField(max_length=2,
                              choices=STATUS_CHOICES,
                              default=NEW)

    def __str__(self):
        return f'Order name: {self.name}, status: {self.status}'

    class Meta:
        db_table = 'orders'
