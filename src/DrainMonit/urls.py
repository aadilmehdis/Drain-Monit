from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details', views.details, name='details'),
    path('sensor/<int:pk>', views.sensor, name='sensor'),
    path('predict', views.predict, name='predict'),
    path('predict_back', views.predict_back, name='predict_back'),
]
