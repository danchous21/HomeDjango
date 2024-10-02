# management/models.py

from django.db import models

class House(models.Model):
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.address

class Apartment(models.Model):
    house = models.ForeignKey(House, related_name='apartments', on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    area = models.DecimalField(max_digits=6, decimal_places=2)  # площадь квартиры

    def __str__(self):
        return f'Apartment {self.number}, House {self.house}'

class WaterMeter(models.Model):
    apartment = models.ForeignKey(Apartment, related_name='water_meters', on_delete=models.CASCADE)
    current_reading = models.DecimalField(max_digits=8, decimal_places=2)  # текущее показание
    previous_reading = models.DecimalField(max_digits=8, decimal_places=2)  # предыдущее показание
    date = models.DateField()

    def __str__(self):
        return f'Meter in Apartment {self.apartment}'

class Tariff(models.Model):
    name = models.CharField(max_length=50)
    price_per_unit = models.DecimalField(max_digits=8, decimal_places=2)  # цена за единицу

    def __str__(self):
        return f'{self.name} - {self.price_per_unit}'
