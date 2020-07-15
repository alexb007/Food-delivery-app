from rest_framework_nested import routers
from apps.foods.viewsets import FoodViewSet, FoodCategoryViewSet
from apps.restaurants.viewsets import RestaurantViewSet, RestaurantTypeViewSet
from apps.orders.viewsets import OrderViewSet, SearchView

router = routers.DefaultRouter()

router.register('restaurants', RestaurantViewSet, base_name='restaurants')
router.register('orders', OrderViewSet, base_name='orders')
router.register('restaurant_types', RestaurantTypeViewSet, base_name='restaurant types')

restaurant_router = routers.NestedDefaultRouter(router, 'restaurants', lookup='restaurant')
restaurant_router.register('categories', FoodCategoryViewSet, base_name='categories')

category_router = routers.NestedDefaultRouter(restaurant_router, 'categories', lookup='category')
category_router.register('foods', FoodViewSet, base_name='foods')
router.register('foods', FoodViewSet, base_name='foods')
