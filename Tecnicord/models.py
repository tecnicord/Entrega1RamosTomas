from django.db import models

class Tractores(models.Model):
    nombre = models.CharField(max_length=40)
    potencia = models.IntegerField()