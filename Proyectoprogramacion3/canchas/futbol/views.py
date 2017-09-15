# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def Inicio(request):
    return render(request , 'inicio.html')
def Login(request):
    return render (request, 'login.html')
def Createuser (request):
    mail=""
    name=""
    password=""
    user = User.objects.create_user(name, mail, password)
    user.save()