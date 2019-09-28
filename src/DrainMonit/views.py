from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):

    context = {}

    return render(request, 'home/index.html', context)

def details(request):

    context = {}
    
    return render(request, 'home/details.html', context)

def predict(request):

    return render(request, 'home/predict.html', context)
