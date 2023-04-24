from django.contrib import admin

from .models import OrderModel


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['name']

    def has_delete_permission(self, request, obj=None):
        return False  # We should not be able to delete objects

    def has_add_permission(self, request):
        return False  # We should not be able to create objects
