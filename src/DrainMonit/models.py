from django.db import models

class Pipe(models.Model):
    MATERIAL = (
        ('HDPE', 'high-density polyethylene'),
        ('PVC', 'polyvinyl chloride'),
        ('Clay', 'clay'),
        ('Concrete', 'concrete'),
        ('Steel', 'steel'),
    )
    location        = models.CharField("Location", max_length=60, null=True)
    diameter        = models.CharField("Diameter", max_length=60, null=True)
    elevation       = models.FloatField("Elevation", null=True)
    material        = models.CharField("Material", max_length=60, choices=MATERIAL)
    color           = models.CharField("Color", max_length=60, null=True)

class Node(models.Model):
    location        = models.CharField("Location", max_length=60, null=True)
    pipe            = models.ForeignKey(Pipe, on_delete=models.CASCADE)

class Name(models.Model):
    location        = models.CharField("Location", max_length=60, null=True)
