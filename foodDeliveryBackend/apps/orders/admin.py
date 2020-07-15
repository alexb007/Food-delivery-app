from django.contrib import admin

from apps.orders.models import Order, OrderProduct


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    pass


class OrderProductInline(admin.StackedInline):
    model = OrderProduct
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('status', 'delivery_type')
    inlines = (OrderProductInline,)
