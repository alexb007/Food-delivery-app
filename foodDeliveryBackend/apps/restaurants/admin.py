from django.contrib import admin
from apps.restaurants.models import Restaurant

# Register your models here.
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'user')
    list_filter = ('user', )
  
