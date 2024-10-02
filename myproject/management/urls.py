# management/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HouseViewSet, ApartmentViewSet, WaterMeterViewSet, TariffViewSet

router = DefaultRouter()
router.register(r'houses', HouseViewSet)
router.register(r'apartments', ApartmentViewSet)
router.register(r'water_meters', WaterMeterViewSet)
router.register(r'tariffs', TariffViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Убедитесь, что нет вложенных включений
]
