from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *

# Create your views here.
def home(request):
    result = Post.objects.all()
    print(result)
    return render(request, 'home.html', {"post_list" : result})

#3-2
def show_post(request):
    contents = Post.objects.all()
    return render(request, 'posts.html', {'post_list' : contents})

def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'detail.html', {"result" : post})

def new(request):
    return render(request, 'new.html')

def create(request):
    post = Post()
    post.user = request.user
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.save()
    return redirect('detail', id = post.id)

def update(request, num):
    post = Post.objects.get(id = num)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.body = request.POST["body"]
        post.save()
        return redirect('detail', id = post.id)
    return render(request, "update.html", {"result" : post})

def delete(request, num):
    post = Post.objects.get(id = num)
    post.delete()
    return redirect('/')

#6-1
def album(request):
    photo = Photo.objects.all()
    return render(request, 'album.html', {"result" : photo})