# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import AnonymousUser, User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.mail import send_mail
from .models import *

# Create your views here.

def Inicio(request):
    return render(request , 'inicio.html')

def Createuser(request):
    lug = Lugar(nombre="Lol 3", cantidad_de_cancha=89, tipo_de_cancha = 1, servicios = "La Dota", telefono=1321654)
    lug.save()
    return render (request, 'createuser.html')

def Createusers (request):
    name=request.POST["usuario"]
    password=request.POST["contrasenia"]
    mail=request.POST["email"]
    user = User.objects.create_user(name, password, mail)
    user.save()
    return render (request, 'createuser.html')
    