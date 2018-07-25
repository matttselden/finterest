from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    if 'user_id' not in request.session:
        request.session['user_id'] = 0
    return render(request, 'finterest_app/index.html')

def login(request):
    return render(request, 'finterest_app/login.html')

def dashboard(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'finterest_app/dashboard.html', context)

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
def logout(request):
    request.session.clear()
    return redirect("/")    

def register(request): 
    print("*" * 50)
    errors = User.objects.basic_validator(request.POST)
    for key, value in errors.items():
        print("errors ", value)
    
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
    #     request.session['first_name'] = request.POST['first_name']
    #     request.session['last_name'] = request.POST['last_name']
    #     request.session['email'] = request.POST['email']
        return redirect('/login')      
  
    # Create addres object
    else: 
        # Create user address
        user_address = Address.objects.create(street_address = request.POST['street_address'] , city=request.POST['city'], state=request.POST['state'], zip_code = request.POST['zip_code'])
        # Hash password
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())  
        # Create new user
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash, bio=request.POST['bio'], user_image=request.FILES['user_image'], address_id = user_address)    
        # Save ID and first name to session
        request.session['user_id'] = new_user.id
        request.session['first_name'] = new_user.first_name
        # Return to user dashboard
        return redirect("/dashboard")

def loginProcess(request):
    errors = User.objects.login_validator(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        request.session['email'] = request.POST['email']
        return redirect('/login')
    else:    
        logedin_user_list = User.objects.filter(email=request.POST['email'])    
        request.session['first_name'] = logedin_user_list[0].first_name
        request.session['user_id'] = logedin_user_list[0].id
        request.session['bio'] = logedin_user_list[0].bio
        request.session['user_image'] = logedin_user_list[0].user_image


        return redirect("/dashboard")
