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
#연결:views.py에서 정의한 함수 써먹기
import testapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', testapp.views.home, name='home'),
    path('about/', testapp.views.about, name='about'),
    path('count/', testapp.views.count, name='count'),
    # '' : route(도메인 뒤에 붙는 url부분)
    # testapp.views.home -> "testapp의 views.py에서 정의내린 home 함수를 실행해주세요"
    # name='home' -> "이 path의 이름을 'home'이라고 할게요!"의 의미. 가급적 함수이름와 name을 일치시켜주자.
]
