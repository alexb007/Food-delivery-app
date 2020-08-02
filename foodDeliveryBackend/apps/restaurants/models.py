from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from apps.users.models import User


class BusinessType(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Business Name'))
    order = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=_('Order in main page')
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Business Type')
        verbose_name_plural = _('Business Type')
        ordering = ('order', 'name')


class RestaurantCategory(models.Model):
    name = models.CharField(max_length=80)
    business = models.ForeignKey(
        BusinessType,
        on_delete=models.CASCADE,
        verbose_name=_('Business')
    )
    icon = models.ImageField(upload_to='restaurants/', default='restaurants/noimage.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Restaurant Type')
        verbose_name_plural = _('Restaurant Types')
        ordering = ('name', '-id',)


class Restaurant(models.Model):
    name = models.CharField(max_length=128)
    address = models.TextField()
    logo = models.ImageField(upload_to='restaurants/', default='restaurants/noimage.png')
    background = models.ImageField(upload_to='restaurants/', default='restaurants/noimage.png')
    type = models.ForeignKey(
        RestaurantCategory,
        on_delete=models.CASCADE,
        null=True,
        related_name='restaurants',
        verbose_name=_("Restaurant Type")
    )
    delivery_price = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    opens = models.TimeField(null=True, blank=True)
    closes = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Restaurant')
        verbose_name_plural = _('Restaurants')
        ordering = ('name', '-id',)
