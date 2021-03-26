from railway_api import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from railway_api.views import *

router = DefaultRouter()
router.register(r'user',views.UserProfileViewSet,base_name='users')
router.register(r'passenger',views.RailwayPassengerViewSet,base_name='passenger')

urlpatterns = [
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register', AuthUserRegistrationView.as_view(), name='register'),
    path('auth/login', AuthUserLoginView.as_view(), name='login'),
    path(r'api/',include(router.urls)),
]