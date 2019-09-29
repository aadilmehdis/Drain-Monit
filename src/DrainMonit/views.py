from django.shortcuts import render
from django.http import HttpResponse
from .models import Sensor, Pipe, Readings
# from .forms import PredictForm
import requests
from .ML.Model import *
import numpy as np
from .replace_json import *


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
    history = Readings.objects.filter(sensor=id)

    if len(history) > 10 :
        history = history[:10]

    rate = []
    date = []

    for tuple in history :
        rate.append( tuple.rate )
        date.append( tuple.date.strftime("%Y-%m-%d") )

    context = {
    's' : sensor,
    'date' : date,
    'rate' : rate,
    }

    return render(request, 'home/sensor.html', context)

def sensor_data(request):

    if request.method == 'POST':
        id = request.POST.get('UID')
        rate = request.POST.get('flow_rate')
        date = request.POST.get('date')
        velocity = request.POST.get('velocity')

        id = Sensor.objects.get(pk=id)
        data = Readings.objects.create(sensor=id, date=date, rate=rate, velocity=velocity)
        html = "<html><p> Received </p></html>"

        return HttpResponse(html)

def predict(request):

    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        form = PredictForm()

    context = {'form': form}

    return render(request, 'home/predict.html', context)

def predict_back(request):
    pipe_list = Pipe.objects.all()
    for pipe in pipe_list:
        X = np.array(
            [float(pipe.elevation), float(pipe.diameter)**2, float(pipe.angle), np.sqrt(np.random.uniform(low=0,high=180)), 1]
        )
        sensor_list = Sensor.objects.filter(pipe=pipe)

        # expected_vel = float(pipe.diameter)**2
        for sensor in sensor_list:
            update_val(sensor.id_name, prediction(X.T), )
    print("Serviced")
    return HttpResponse("Yello")
