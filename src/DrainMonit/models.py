from django.db import models

class Pipe(models.Model):
    LOCATION = (
        ('A','a'),
        ('B','b'),
        ('C','c'),
        ('D','d'),
        ('E','e'),
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

    def __str__(self):
        return "Pipe: {} {}".format(self.pk, self.location)

class Sensor(models.Model):
    pipe                    = models.ForeignKey(Pipe, on_delete=models.CASCADE)
    id_name                 = models.CharField("ID Name", max_length=60, null=True)                 

    def __str__(self):
        return "Sensor: {} {}".format(self.pk, self.pipe)

class Readings(models.Model):
    sensor                  = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    date                    = models.DateField("Date", null=True)
    rate                    = models.FloatField("Rate", null=True)
    velocity                = models.FloatField("Velocity", null=True)

    def __str__(self):
        return "Readings: {} {}".format(self.pk, self.sensor)
