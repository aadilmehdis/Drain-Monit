from django.shortcuts import render
from django.http import HttpResponse
from .models import Sensor, Pipe
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

    context = {
    's' : sensor,
    'history' : ''
    }

    return render(request, 'home/sensor.html', context)

def predict(request):

    context = {}
    
    return render(request, 'home/predict.html', context)

def predict_back(request):
    pass
