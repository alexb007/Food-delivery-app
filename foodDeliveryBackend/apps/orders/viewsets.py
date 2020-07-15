from rest_framework import viewsets, mixins, views
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Order, OrderProduct
from .serializers import OrderSerializer
from ..foods.models import Food
from ..foods.serializers import FoodSerializer
from ..restaurants.models import Restaurant
from ..restaurants.serializers import RestaurantSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class SearchView(views.APIView):
    def post(self, request, *args, **kwargs):
        query = request.data.get('q', None)
        if query:
            restaurants = Restaurant.objects.filter(name__icontains=query)[:5]
            foods = Food.objects.filter(name__icontains=query)[:5]
            return Response({
                'restaurants': RestaurantSerializer(restaurants, many=True).data,
                'foods': FoodSerializer(foods, many=True).data
            })
        return Response({
            'error': 'Введите фразу для поиска'
        })
