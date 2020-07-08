from django.contrib import admin
from apps.restaurants.models import Restaurant, RestaurantType


# Register your models here.

@admin.register(RestaurantType)
class RestaurantTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('user',)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'user', 'type', 'opens', 'closes')
    list_filter = ('user', 'type')
