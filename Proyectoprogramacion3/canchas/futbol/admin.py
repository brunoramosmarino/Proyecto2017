# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (Lugar, Cancha, Reservacion)
# Register your models here.

admin.site.register(Lugar)
admin.site.register(Cancha)
admin.site.register(Reservacion)