from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Signup

# Create your views here.

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST['username'], password = request.POST['password1']
            )
            signup = Signup()
            signup.major = request.POST['major']
            signup.phone = request.POST['phone']
            signup.user = user
            signup.save()
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')
    # {% url 'signup' %}

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error' : "username or password is not correct"})
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    user = request.user
    sign = Signup.objects.get(user = user)
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            sign.phone = request.POST['phone']
            sign.major = request.POST['major']
            user.set_password(request.POST['password1'])
            sign.save()
            user.save()
            return redirect('/')
    return render(request, 'profile.html', {"profile" : sign})