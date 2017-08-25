# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Lugar(models.Model):
    nombre = models.CharField(max_legth=30)
    cantidad_de_cancha = models.IntegerField()
    tipo_de_cancha = models.IntegerField()
    servicios = models.CharField()
    telefono = models.IntegerField()
    horario = models.IntegerField()
    

class Cancha(models.model):
    lugar=models.ForeignKey(Lugar)
    numero_de_cancha = models.IntegerField()
    tipo = models.CharField()
    precio = models.IntegerField()
    
class Resevacion(models.model):
    id_reservacion = models.PrimaryKey()
    cancha = models.ForeingKey(Cancha)
    fecha = models.DataTime()
    