from django.db import models

# Create your models here.
class Post(models.Model):
    "id = int => 각 게시물에 고유한 번호를 배정. 학번 같은 느낌임"
    title = models.CharField(max_length = 20)
    #title이라는 열을 만들고 models -> Char(제한적 길이를 가진 문자) -> max_length
    body = models.TextField()    #body라는 열을 만들고 Text(제한이 없는 문자열)
    pub_date = models.DateTimeField('published time')
    #pub_date라는 열을 만들고, 그 형식을 날짜/시간의 형태로 넣겠다.

    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    img = models.ImageField(upload_to="album/") #media 폴더 안에 album 폴더를 만들고 거기에 넣어줌.
    
    def __str__(self):
        return self.title
    #"python manage.py makemigrations -> 파이썬으로 작성된 것을 DB 언어로 바꿔준다."
    #"python manage.py migrate -> DB에 적용"

        #Pillow -> 파이썬에서 이미지파일을 다루기 위한 라이브러리.
        #DB -> 이미지 자체로 저장을 할 수가 없어서 알아들을 수 있게 변환하는 프로그램이 필요함.그게 Pillow.
        #새롭게 해준 후에, python manage.py makemigrations -> python manage.py migrate 순으로 ㄱㄱ


    #models.py에서
    #class 테이블 이름(models.Model):
        #열 이름 = models.[데이터 열]
        #def __str__(self):
            #return self.title
    #"python manage.py makemigrations -> 파이썬으로 작성된 것을 DB 언어로 바꿔준다."
    #"python manage.py migrate -> DB에 적용"
    #그 이후에 /admin -> login 하라고 함. python manage.py createsuperuser
    #그 이후 admin.py에서, admin.site.register(Post)
    #html에 띄워야 되니까 .. views.home에 가서 result = Post.objects.all() -> 정의한 DB 테이블을 가져와서 모든 객체를 가져왔음.
    #이걸 변수로 담아서 home.html에 줬고, html에서 for문을 이용해서 for i in 테이블: i.title 이런 식으로 넣어 줬음.
    #views에서 detail 함수를 정의해준 후 detail.html을 만들어 줬음
    #'detail/<int:변수>'.views.detail().....
    #detail(request):
    #detail(request, 변수=번수)
    #그 이후에 views.py로 가서 detail 함수를 바꿔줌. (detail(request, "변수") 이런식으로 변수를 추가해줘서 2개를 받게 함)
    #그 이후, 변수 추출을 .. view.py에 detail 함수에서 post.objects.get(id="변수")
    #return render(request, 'detail.html', {'content' : content}) 이런식으로 "detail.html" 을 추가해줌.
    # "{% url 'detail' post.id %}"을 home.html에다가 적어주고 ..
    #그 이후 detail.html에서 {{result.title}}, {{result.pub_date}} 이런 식으로 받아준 것.
    #마지막으로, home.html로 돌아가는 건, <a href="{% url 'home' %}">home으로 가기</a> 이런 식으로 써주면 된다. 다른 값을 받아 올 필요가 없기 때문.
