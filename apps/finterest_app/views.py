from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, 'finterest_app/index.html')

def login(request):
    return render(request, 'finterest_app/login.html')

def dashboard(request):
    return render(request, 'finterest_app/dashboard.html')

def addnewfave(request):
    return render(request, 'finterest_app/addnewfave.html')