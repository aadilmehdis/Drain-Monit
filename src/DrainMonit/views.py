from django.shortcuts import render
from django.http import HttpResponse
from .models import Sensor, Pipe, Readings
import requests


def index(request):

    context = {}

    return render(request, 'home/index.html', context)

def details(request):

    all_sensors = Pipe.objects.all()

    context = {
    'sensors' : all_sensors,
    }

    return render(request, 'home/details.html', context)


def sensor(request, pk=None):

    sensor = Pipe.objects.get(pk=pk)
    id = Sensor.objects.get(pk=pk)
    history = Readings.objects.get(sensor=id)
    print(history)
    context = {
    's' : sensor,
    'history' : history
    }

    return render(request, 'home/sensor.html', context)

def sensor_data(request):

    if request.method == 'POST':
        id = request.POST.get('UID')
        rate = request.POST.get('flow_rate')
        date = request.POST.get('date')
        print(id, rate, date)

        id = Sensor.objects.get(pk=id)
        data = Readings.objects.create(sensor=id, date=date, rate=rate)
        html = "<html><p> Received </p></html>"

        return HttpResponse(html)

def predict(request):

    context = {}

    return render(request, 'home/predict.html', context)

def predict_back(request):
    print(request)
    return HttpResponse("Yello")
