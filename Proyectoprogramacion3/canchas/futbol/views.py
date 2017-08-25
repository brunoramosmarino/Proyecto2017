# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.
def Inicio(request):
    return render(request , 'inicio.html')
def Login(request):
    return render (request, 'login.html')