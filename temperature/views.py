from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import TemperatureReading

def temperature_data(request):
    temperature_readings = TemperatureReading.objects.all()
    data = [{'timestamp': reading.timestamp, 'temperature': reading.temperature} for reading in temperature_readings]
    return JsonResponse(data, safe=False)
