# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def Inicio(request):
    return render(request , 'inicio.html')
def Createuser(request):
    return render (request, 'createuser.html')
def Createusers (request):
    name=request.POST["usuario"]
    password=request.POST["contraseña"]
    mail=request.POST["email"]
    print name + password
    user = User.objects.create_user(username="bruno", email="bruno@gmail.com", password="hola")
    user.save()
    return (request, 'createuser.html')