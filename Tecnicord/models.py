from django.db import models

class Tractores(models.Model):
    nombre = models.CharField(max_length=40)
    potencia = models.IntegerField()

class Camiones(models.Model):
    nombre = models.CharField(max_length=40)
    carga = models.IntegerField()

class Pulverizadoras(models.Model):
    nombre = models.CharField(max_length=40)
    litros = models.IntegerField()