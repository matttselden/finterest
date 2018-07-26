from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    if 'user_id' in request.session:
        return redirect("/dashboard/"+str(request.session['user_id']))
    else:
        return render(request, 'finterest_app/index.html')

def login(request):
    # if 'user_id' in request.session:
    #     return redirect("/dashboard/"+str(request.session['user_id']))
    # else:
    return render(request, 'finterest_app/login.html')

def dashboard(request, idnumber):
    if 'user_id' in request.session:
        context = {
            "users": User.objects.exclude(followed_by__follower_id = request.session['user_id']).exclude(id=request.session['user_id']),
            "dashuser": User.objects.get(id=idnumber),
            'activities': Favorite.objects.filter(category='activity').filter(comments__user_id=idnumber).order_by('-id')[:3],
            'restaurants': Favorite.objects.filter(category='restaurant').filter(comments__user_id=idnumber).order_by('-id')[:3],
            'places': Favorite.objects.filter(category='place').filter(comments__user_id=idnumber).order_by('-id')[:3],
            'following': User.objects.filter(followed_by__follower_id = request.session['user_id']),
        }
        return render(request, 'finterest_app/dashboard.html', context)
    else:
        messages.error(request, 'Must be logged in to view the dashboard', 'login')
        return redirect('/login')

def addnewfave(request):
    if 'user_id' in request.session:
        context = {
            "users": User.objects.exclude(followed_by__follower_id = request.session['user_id']).exclude(id=request.session['user_id']),
            "following": User.objects.filter(followed_by__follower_id = request.session['user_id']),
        }
        return render(request, 'finterest_app/addnewfave.html', context)
    else:
        messages.error(request, 'Must be logged in to view the dashboard', 'login')
        return redirect('/login')

def createfave(request):
    fav = Favorite.objects.create(
        name = request.POST['name'],
        description = request.POST['description'],
        category = request.POST['category'],
        favorite_image = request.FILES['pic'],
        address_id = Address.objects.create(street_address=request.POST['street'], city=request.POST['city'], state=request.POST['state'], zip_code=request.POST['zip'])
    )
    Comment.objects.create(
        comment = request.POST['comment'],
        favorite_id_id = fav.id,
        user_id_id = request.session['user_id']
    )
    return redirect("/dashboard/"+str(request.session['user_id']))
    
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
            messages.error(request, value, extra_tags = key)
        messages.info(request, request.POST['first_name'], extra_tags = 'fn_input')
        messages.info(request, request.POST['last_name'], extra_tags = 'ln_input')
        messages.info(request, request.POST['email'], extra_tags = 'e_input')
        messages.info(request, request.POST['street_address'], extra_tags = 'sa_input')
        messages.info(request, request.POST['city'], extra_tags = 'c_input')
        messages.info(request, request.POST['state'], extra_tags = 's_input')
        messages.info(request, request.POST['zip_code'], extra_tags = 'zc_input')
        print(request.POST['bio'])
        messages.info(request, request.POST['bio'], extra_tags = 'b_input')
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
        return redirect("/dashboard/"+str(request.session['user_id']))

def loginProcess(request):
    errors = User.objects.login_validator(request.POST)
    print(errors)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags = key)
        request.session['email'] = request.POST['email']
        return redirect('/login')
    else:    
        logedin_user_list = User.objects.filter(email=request.POST['email'])    
        request.session['first_name'] = logedin_user_list[0].first_name
        request.session['user_id'] = logedin_user_list[0].id
        return redirect("/dashboard/"+str(request.session['user_id']))

def follow(request, idnumber):
    dashuser=User.objects.get(id=idnumber)
    curruser=User.objects.get(id=request.session['user_id'])
    Follower.objects.create(follower=curruser, followed=dashuser)
    return redirect('/dashboard/'+idnumber)

def unfollow(request, idnumber):
    dashuser=User.objects.get(id=idnumber)
    curruser=User.objects.get(id=request.session['user_id'])
    b = Follower.objects.get(follower=curruser, followed=dashuser)
    b.delete()
    return redirect('/dashboard/'+idnumber)

def editprofile(request):
    if 'user_id' in request.session:
        context = {
            "users": User.objects.exclude(followed_by__follower_id = request.session['user_id']).exclude(id=request.session['user_id']),
            "dashuser": User.objects.get(id=request.session['user_id']),
            'activities': Favorite.objects.filter(category='activity').filter(comments__user_id=request.session['user_id']).order_by('-id')[:3],
            'restaurants': Favorite.objects.filter(category='restaurant').filter(comments__user_id=request.session['user_id']).order_by('-id')[:3],
            'places': Favorite.objects.filter(category='place').filter(comments__user_id=request.session['user_id']).order_by('-id')[:3],
            'following': User.objects.filter(followed_by__follower_id = request.session['user_id']),
        }
        return render(request, 'finterest_app/editprofile.html', context)
    else:
        messages.error(request, 'Must be logged in to view the dashboard', 'login')
        return redirect('/login')