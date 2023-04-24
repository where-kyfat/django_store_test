from django.contrib import admin

from .models import OrderModel


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'status')

    def get_readonly_fields(self, request, obj=None):
        # Admin panel should be able to changes values while create new Order
        if obj:
            return self.readonly_fields
        return ()

    def has_change_permission(self, request, obj=None):
        # Admin panel should only create Orders
        if obj:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False  # We should not be able to delete objects

