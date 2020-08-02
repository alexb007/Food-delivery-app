from django.contrib import admin
from apps.restaurants.models import Restaurant, RestaurantCategory, BusinessType


# Register your models here.
@admin.register(BusinessType)
class BusinessTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')


@admin.register(RestaurantCategory)
class RestaurantTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'user', 'type', 'opens', 'closes')
    list_filter = ('user', 'type')
