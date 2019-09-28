from django.contrib import admin
from DrainMonit.models import Pipe, Sensor

# Register your models here.
admin.site.register(Sensor)
admin.site.register(Pipe)
