from django.shortcuts import render
from django.http import HttpResponse
from .models import Sensor, Pipe, Readings
# from .forms import PredictForm
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

        id = Sensor.objects.get(pk=id)
        data = Readings.objects.create(sensor=id, date=date, rate=rate)
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
    print(request)
    return HttpResponse("Yello")
