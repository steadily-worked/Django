from django.shortcuts import render, redirect
from .models import Post # 우리가 이전에 정의해 둔 Post라는 표를 가져오겠다는 의미이다.
from django.utils import timezone

# Create your views here.
# "함수" : "요청이 들어오면 제가 만든 html 화면을 띄워주세요!"의 의미임

def home(request):
    result = Post.objects.all()
    print(result)
    return render(request, 'home.html', {"post_list" : result})
#home이라는 함수:
#   요청이 들어오면 home.html을 열어주세요!

def about(request):
    return render(request, 'about.html')

def count(request):
    entered_text = request.GET['fulltext'] #데이터를 가공하는 코드.
    # 요청(request)이 들어오면, 가져와라(GET) ['fulltext']를.
    # 여기서 fulltext는, textarea의 name으로 설정해뒀던 것이다.
    word_list = entered_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
        # 이 for문을 다 돌면, word_dictionary 안에는 사용자가 입력한 텍스트와 단어와 그 단어의 출현횟수를
        # {'단어' : 출현횟수}의 형태로 모두 저장한다.

    return render(request, 'count.html', {'alltext' : entered_text, 'total' : len(word_list), 'dictionary' : word_dictionary.items()})
    # {}부분 : 이런 데이터들도 count.html에 넘겨주겠다고 선언해주는 것.
    # 여기서 alltext는, entered_text를 쓰긴 쓰는데 count.html에서 쓸 때 이런 이름(alltext)으로
    # 쓰겠다는 의미이다. urls.py에서 path이름 설정해주는 과정과 비슷하다고 생각하면 됨.
    # 이후에 count.html에서 alltext를 써보는 과정으로 간다.
def show_post(request):
    contents = Post.objects.all()
    # Post(표)에서 objects(행)을 all(모두) 가져오겠다는 것이다. 작성한 글들이 List로 담겨온다.
    # 이를 contents 라는 변수에 저장해둔다.
    return render(request, 'posts.html', {'post_list' : contents}) #html에 post_list라는 이름으로 넘겨준다.
    # 여기까지가 views에서 posts.html에 데이터를 넘겨주는 과정이었음.

def new(request):
    return render(request, 'new.html')

def create(request):
    post = Post() #models.py에서 만든 Post라는 테이블에서 필드들의 값이 비어있는 행을 하나 만드는 코드
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('/detail/'+str(post.id)) # 해당 데이터 detail을 보여주는 앞전 urls.py에서 설정했던 detail/<int:pk> url로 보내버려 라고 되는 것.
    # 여기선 render이 아니라 redirect를 쓰고있는데, redirect는 요청을 처리하고 보여주는 페이지임.
    # render가 '요청이 들어오면 이 html 파일을 보여줘' 라는 뜻이라면,
    # redirect는 '요청이 들어오면 저쪽 url로 보내버려' 라는 뜻이다.
    # (redirect - urls.py에 있는 것중 하나 불러오기, render - templates에 있는 html 보여주기)
def detail(request, num):
    content = Post.objects.get(id=num)
    return render(request, 'detail.html', {'content' : content})

def update(request, num): #urls.py에서 넘어오는 num을 매개변수로 추가하여 받을 준비를 함
    post = Post.objects.get(id = num) # detail 함수에서와 같이 글의 id가 num과 같은 것을 찾아 post라는 변수에 담음
    if request.method == "POST":
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
        return redirect('/detail/' + str(num))
    return render(request, 'update.html', {"result" : post})
    #result : post는 .. post 변수를 result 라는 이름으로 update.html로 넘겨줌
    pass

def delete(request, num):
    post = Post.objects.get(id = num)
    post.delete()
    return redirect('/')

def album(request):
    return render(request, 'album.html')