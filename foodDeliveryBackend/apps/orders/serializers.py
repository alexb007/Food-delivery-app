from rest_framework import serializers

from apps.foods.serializers import FoodProductSerializer
from apps.orders.models import Order, OrderProduct


class OrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderProduct
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        for product_data in products_data:
            print(product_data)
            OrderProduct.objects.create(order=order, **product_data)
        return order
