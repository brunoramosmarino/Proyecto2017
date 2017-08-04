# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cancha(models.Model):
    nombre = models.CharField(max_legth=30)
    cantidad = models.IntegerField()
    servicios = models.CharField()
    tipos = models.CharField()

