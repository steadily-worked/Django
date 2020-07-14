from django.shortcuts import render, redirect
from .models import Post, Album
from django.utils import timezone

# Create your views here.
def home(request):
    result = Post.objects.all()
        #Post.objects() : 표 전체
        #Post.objects.all() : 표 내에 행 전체 ...
        #.all => 게시물의 행들을 list로 가져와 준다. => 메소드(객체를 다루는 함수들)
        #.filter(), .order_by() => 다 메소드임.
        #QuerySet => 쿼리(요청) => set. DB가 준 것을 Set하는 과정.
    print(result)
    return render(request, 'home.html', {"post_list" : result})

def detail(request, num):
 #값이 리스트로 넘어옴. => 여러개를 추출해줄 수 있다.
    content = Post.objects.get(id=num) #행 id가 num인 것을 1개 준다.
    return render(request, 'detail.html', {'content' : content})

def new(request):
    return render(request, 'new.html')

def create(request):
    post = Post()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('detail', num = post.id)

def update(request, num):
    post = Post.objects.get(id=num)
    if request.method == "POST":
        #수정된 글을 저장해주겠다
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
        return redirect('/detail/' + str(post.id))
    #수정된 글을 보내주겠다.
    return render(request, 'update.html', {"result" : post})
    pass

def delete(request, num):
    post = Post.objects.get(id = num)
    post.delete()
    return redirect('/')

def album(request):
    img = Album.objects.all()
    return render(request, 'album.html', {"images" : img})
