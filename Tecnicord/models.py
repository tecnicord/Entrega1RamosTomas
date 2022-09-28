from django.db import models

class Tractores(models.Model):
    nombre = models.CharField(max_length=40)
    potencia = models.IntegerField(unique=True)

    def __str__(self):
        return f"Tractores: {self.nombre}, Potencia: {self.potencia}"


class Camiones(models.Model):
    nombre = models.CharField(max_length=40)
    carga = models.IntegerField(unique=True)

    def __str__(self):
        return f"Camiones: {self.nombre}, Carga: {self.carga}"

class Pulverizadoras(models.Model):
    nombre = models.CharField(max_length=40)
    litros = models.IntegerField(unique=True)

    def __str__(self):
        return f"Pulverizadoras: {self.nombre}, Litros: {self.litros}"
