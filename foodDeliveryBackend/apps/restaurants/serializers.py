from rest_framework import serializers
from .models import Restaurant, RestaurantCategory, BusinessType
from apps.foods.serializers import FoodCategorySerializer, FoodSerializer
from apps.foods.models import FoodCategory


class BusinessTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessType
        fields = ('id', 'name', 'order')


class RestaurantTypeSerializer(serializers.ModelSerializer):
    business = BusinessTypeSerializer()

    class Meta:
        model = RestaurantCategory
        fields = ('id', 'name', 'icon', 'business')


class RestaurantSerializer(serializers.ModelSerializer):
    categories = FoodCategorySerializer(many=True, read_only=True)
    type = RestaurantTypeSerializer()

    def __init__(self, *args, **kwargs):
        # initialize fields
        fields = kwargs.pop('fields', None)
        super(RestaurantSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'categories', 'opens', 'closes', 'type', 'logo', 'background')


class RestaurantRetrieveSerializer(serializers.ModelSerializer):
    categories = FoodCategorySerializer(many=True, read_only=True)
    foods = FoodSerializer(many=True, read_only=True)
    type = RestaurantTypeSerializer()

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'categories', 'opens', 'closes', 'type', 'logo', 'background', 'foods')
