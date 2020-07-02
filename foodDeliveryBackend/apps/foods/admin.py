from django.contrib import admin

from apps.foods.models import FoodCategory, Food

# Register your models here.
@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant')
    list_filter = ('restaurant')
    
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'restaurant', 'active', 'price')
    list_filter = ( 'category', 'restaurant')
    
