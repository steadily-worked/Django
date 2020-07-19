from django.shortcuts import render

# Create your views here.
# "함수" : "요청이 들어오면 제가 만든 html 화면을 띄워주세요!"의 의미임

def home(request):
    return render(request, 'home.html')
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