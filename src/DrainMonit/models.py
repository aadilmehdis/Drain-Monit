from django.db import models

class Pipe(models.Model):
    LOCATION = (
        ('A','a'),
        ('B','b'),
        ('C','c'),
        ('D','d'),
    )
    MATERIAL = (
        ('high-density polyethylene', 'HDPE'),
        ('polyvinyl chloride', 'PVC'),
        ('clay', 'CLY'),
        ('concrete', 'CNCRT'),
        ('Steel', 'STL'),
    )
    location                = models.CharField("Location", max_length=60, choices=LOCATION)
    diameter                = models.CharField("Diameter", max_length=60, null=True)
    angle                   = models.FloatField("Angle", null=True)
    material                = models.CharField("Material", max_length=60, choices=MATERIAL)
    elevation               = models.FloatField("Elevation", null=True)

class Sensor(models.Model):
    pipe                    = models.ForeignKey(Pipe, on_delete=models.CASCADE)
    history                 = models.FloatField("Reading History", null=True)
