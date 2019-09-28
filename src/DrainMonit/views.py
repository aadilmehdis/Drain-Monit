from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):

    context = {}

    return render(request, 'home/index.html', context)

def monitor(request):

    return render(request, 'home/monitor.html', context)

def predict(request):

    return render(request, 'home/predict.html', context)
