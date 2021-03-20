from railway_api import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('railway',views.UserProfileViewSet,base_name='')

urlpatterns = [
    path('',include(router.urls))
]