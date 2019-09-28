from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('monitor', views.monitor, name='monitor'),
    path('predict', views.predict, name='predict'),
]
