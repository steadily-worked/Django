from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Signup

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST['username'], password= request.POST['password1']
            )
            signup = Signup()
            signup.user = user
            signup.std_num = request.POST['std_num']
            signup.major = request.POST['major']
            signup.phone = request.POST['phone']
            signup.save()
            auth.login(request, user)         
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    user = request.user
    profile = Signup.objects.get(user=user)
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user.set_password(request.POST['password1'])
            profile.std_num = request.POST['std_num']
            profile.major = request.POST['major']
            profile.phone = request.POST['phone']
            user.save()
            profile.save()
            return redirect('home')
    else:
        return render(request, 'profile.html', {"profile" : profile})