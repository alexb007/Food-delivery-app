from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Restaurant, RestaurantCategory, BusinessType
from .serializers import RestaurantSerializer, RestaurantTypeSerializer, RestaurantRetrieveSerializer, \
    BusinessTypeSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from ..foods.serializers import FoodSerializer


class BusinessesViewSet(viewsets.ModelViewSet):
    queryset = BusinessType.objects.all().order_by('order')
    serializer_class = BusinessTypeSerializer

    def list(self, request, **kwargs):
        if request.query_params == {}:
            queryset = BusinessType.objects.all()
        else:
            query = request.query_params['search']
            queryset = BusinessType.objects.filter(name__icontains=query)
        serializer = BusinessTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class RestaurantTypeViewSet(viewsets.ModelViewSet):
    queryset = RestaurantCategory.objects.all()
    serializer_class = RestaurantTypeSerializer

    def list(self, request):
        if request.query_params == {}:
            queryset = RestaurantCategory.objects.all()
        else:
            query = request.query_params['search']
            queryset = RestaurantCategory.objects.filter(name__icontains=query)

        serializer = RestaurantTypeSerializer(
            queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all().prefetch_related(
        'categories', 'categories__foods')
    serializer_class = RestaurantSerializer
    filter_backends = (SearchFilter,)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RestaurantRetrieveSerializer
        return self.serializer_class

    def list(self, request):

        if request.query_params == {}:
            queryset = Restaurant.objects.all()
        else:
            name = request.query_params.get('search', None)
            rest_type = request.query_params.get('type', None)
            filters = {}
            if name:
                filters['name__icontains'] = name
            if rest_type:
                filters['type'] = rest_type
            queryset = Restaurant.objects.filter(**filters)

        serializer = RestaurantSerializer(
            queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        if not request.user.is_restaurant:
            return Response({'message': 'unauthorized'}, 401)

        serializer = RestaurantSerializer(
            data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save(user=request.user)

        return Response(serializer.data)

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'foods']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    @action(methods=['get'], detail=True)
    def foods(self, request, *args, **kwargs):
        foods = self.get_object().foods.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)
