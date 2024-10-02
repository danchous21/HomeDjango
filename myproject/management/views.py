# management/views.py

from rest_framework import viewsets
from .models import House, Apartment, WaterMeter, Tariff
from .serializers import HouseSerializer, ApartmentSerializer, WaterMeterSerializer, TariffSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page!")
class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class WaterMeterViewSet(viewsets.ModelViewSet):
    queryset = WaterMeter.objects.all()
    serializer_class = WaterMeterSerializer

class TariffViewSet(viewsets.ModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer
