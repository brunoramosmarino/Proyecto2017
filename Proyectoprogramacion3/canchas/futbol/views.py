# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
# Create your views here.
<<<<<<< HEAD
def Inicio(request):
=======

def inicio(request):
>>>>>>> 95521ea7a9ec20dca12417ac57e25c6eddb78935
    return render(request , 'inicio.html')

def createuser(request):

    return render (request, 'createuser.html')

def lugar(request):
    return render (request, 'Lugar.html')
def createlugar(request):
    nombre=request.POST['nombre_de_lugar']
    cantidad=request.POST['cantidad_de_canchas']
    tipo=request.POST['tipo_de_canchas']
    telefono=request.POST['telefono']
    horario=request.POST['horarios']
    servicios=request.POST['servicios']
    lug = Lugar(nombre=nombre, cantidad_de_cancha=cantidad, tipo_de_cancha = tipo, servicios = servicios, telefono=telefono, horario=horario)
    lug.save()    
    return render (request, 'Lugar.html')

def createusers (request):
    name=request.POST["usuario"]
    password=request.POST["contraseña"]
    mail=request.POST["email"]
<<<<<<< HEAD
    print name + password
    user = User.objects.create_user(username=name, password=password, email=mail)
    user.save()
    return HttpResponse("Funca")


     
=======
    user = User.objects.create_user(name, password, mail)
    user.save()
    return render (request, 'createuser.html')

>>>>>>> 95521ea7a9ec20dca12417ac57e25c6eddb78935
