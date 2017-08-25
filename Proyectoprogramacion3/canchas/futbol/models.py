# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Lugar(models.Model):
    nombre = models.CharField(max_length=30)
    cantidad_de_cancha = models.IntegerField()
    tipo_de_cancha = models.IntegerField()
    servicios = models.CharField(max_length=30)
    telefono = models.IntegerField()
    horario = models.IntegerField()
    

class Cancha(models.Model):
    lugar=models.ForeignKey(Lugar)
    numero_de_cancha = models.IntegerField()
    tipo = models.CharField(max_length=30)
    precio = models.IntegerField()
    
class Reservacion(models.Model):
    cancha = models.ForeignKey(Cancha)
    fecha = models.DateTimeField()
