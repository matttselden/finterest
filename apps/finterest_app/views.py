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

def createfave(request):
    Favorite.objects.create(
        name = request.POST['name'],
        description = request.POST['description'],
        category = request.POST['category'],
        favorite_image = request.POST['pic'],
        address_id = Address.objects.create(street_address=request.POST['street'], city=request.POST['city'], state=request.POST['state'], zip_code=request.POST['zip'])
    )
    return redirect('/dashboard')