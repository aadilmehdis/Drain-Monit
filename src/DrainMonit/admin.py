from django.contrib import admin
from DrainMonit.models import Pipe, Sensor, Readings

admin.site.register(Sensor)
admin.site.register(Pipe)
admin.site.register(Readings)
