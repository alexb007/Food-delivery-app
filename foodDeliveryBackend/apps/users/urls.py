from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import register_restaurant, register_customer, token, refresh_token, revoke_token, me

urlpatterns = [
    path('me/', me),
    path('register/customer', register_customer),
    path('register/restaurant', register_restaurant),
    # path('token/', token),
    # path('token/refresh/', refresh_token),
    path('token/revoke/', revoke_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
