from django.db import models
from django_fsm import FSMField


class Order(models.Model):
    DELIVER = 'deliver'
    SELF_PICK = 'self'

    DELIVERY_TYPES = (
        (DELIVER, 'Delivery'),
        (SELF_PICK, 'Self pick'),
    )

    STATUS_DRAFT = 'draft'
    STATUS_SUBMITTED = 'submitted'
    STATUS_CANCELED = 'canceled'
    STATUS_IN_PROGRESS = 'inprogress'
    STATUS_READY = 'ready'
    STATUS_ONROAD = 'onroad'
    STATUS_DELIVERED = 'delivered'
    STATUS_COMPLETED = 'completed'
    STATUS_PAYED = 'payed'
    STATUS_COMMENTED = 'commented'

    STATUSES = (
        (STATUS_DRAFT, STATUS_DRAFT),
        (STATUS_SUBMITTED, STATUS_SUBMITTED),
        (STATUS_CANCELED, STATUS_CANCELED),
        (STATUS_IN_PROGRESS, STATUS_IN_PROGRESS),
        (STATUS_READY, STATUS_READY),
        (STATUS_ONROAD, STATUS_ONROAD),
        (STATUS_DELIVERED, STATUS_DELIVERED),
        (STATUS_COMPLETED, STATUS_COMPLETED),
        (STATUS_PAYED, STATUS_PAYED),
        (STATUS_COMMENTED, STATUS_COMMENTED),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at"
    )

    phone = models.CharField(
        max_length=13,
        verbose_name='Phone number',
    )
    contact_name = models.CharField(
        max_length=100,
        verbose_name='Contact name'
    )
    comment = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name='Comment'
    )
    delivery_type = models.CharField(
        default=DELIVER,
        choices=DELIVERY_TYPES,
        max_length=16,
        verbose_name="Delivery type"
    )

    status = FSMField(choices=STATUSES, default=STATUS_SUBMITTED)

    def __str__(self):
        return f'Order #{self.id}'

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderProduct(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        null=True,
        related_name='products',
        verbose_name='Order'
    )
    product = models.ForeignKey(
        'foods.Food',
        on_delete=models.CASCADE,
        related_name='ordered_products',
        verbose_name='Product'
    )
    amount = models.FloatField(
        verbose_name='Amount'
    )
    comment = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.product.name}'

    class Meta:
        verbose_name = 'Order Product'
        verbose_name_plural = 'Order Products'
