# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Lugar(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    cantidad_de_cancha = models.IntegerField(null=False)
    tipo_de_cancha = models.CharField(max_length=200, null=False)
    servicios = models.CharField(max_length=500, null=False)
    telefono = models.IntegerField(null=False)
    horario = models.CharField(max_length=100, null=False)
    

class Cancha(models.Model):
    lugar=models.ForeignKey(Lugar)
    numero_de_cancha = models.IntegerField()
    tipo = models.CharField(max_length=30)
    precio = models.IntegerField()
    
class Reservacion(models.Model):
    cancha = models.ForeignKey(Cancha)
    fecha = models.DateTimeField()
