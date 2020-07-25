from rest_framework import serializers
from .models import Restaurant, RestaurantType
from apps.foods.serializers import FoodCategorySerializer, FoodSerializer
from apps.foods.models import FoodCategory


class RestaurantTypeSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()
    class Meta:
        model = RestaurantType
        fields = ('id', 'name', 'icon')

    def get_icon(self, obj):
        request = self.context.get('request')
        icon_url = obj.icon.url
        return request.build_absolute_uri(icon_url)


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
