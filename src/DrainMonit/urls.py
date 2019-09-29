from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details', views.details, name='details'),
    path('sensor/<int:pk>', views.sensor, name='sensor'),
    path('sensor_data', views.sensor_data, name='sensor_data'),
    path('predict', views.predict, name='predict'),
]
