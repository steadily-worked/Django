"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views
#연결:views.py에서 정의한 함수 써먹기
from django.conf import settings
from django.conf.urls.static import static
import testapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('count/', views.count, name='count'),
    path('post/', views.show_post, name='post'),
    path('new/', views.new, name='new'),
    path('detail/<int:num>', views.detail,name='detail'),
    path('new/create', views.create, name='create'),
    path('update/<int:num>', views.update, name='update'), # 글의 id를 num이라는 변수로 받겠다는 것.
    path('delete/<int:num>', views.delete, name='delete'),
    path('album/', views.album, name='album')
    # '' : route(도메인 뒤에 붙는 url부분)
    # testapp.views.home -> "testapp의 views.py에서 정의내린 home 함수를 실행해주세요"
    # name='home' -> "이 path의 이름을 'home'이라고 할게요!"의 의미. 가급적 함수이름와 name을 일치시켜주자.
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)