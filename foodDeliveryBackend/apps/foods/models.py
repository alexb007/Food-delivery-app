from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.translation import gettext_lazy as _

from apps.restaurants.models import Restaurant


class FoodCategory(models.Model):
    name = models.CharField(max_length=50)
    restaurant = models.ForeignKey(
        Restaurant, related_name="categories", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Food Category')
        verbose_name_plural = _('Food Categories')


class Food(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        FoodCategory, related_name="foods", on_delete=models.CASCADE)
    restaurant = models.ForeignKey(
        Restaurant, related_name="foods", on_delete=models.CASCADE)
    description = models.TextField()
    cover = models.ImageField(upload_to='foods/', null=True, blank=True)
    active = models.BooleanField()
    price = models.PositiveIntegerField()
    is_veg = models.BooleanField()
    quantity = JSONField(default=dict, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Food Category')
        verbose_name_plural = _('Food Categories')
