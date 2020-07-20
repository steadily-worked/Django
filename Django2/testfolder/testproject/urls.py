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
import testapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', testapp.views.home, name='home'),
    path('post/', testapp.views.show_post, name='post'),
    path('detail/<int:id>', testapp.views.detail, name='detail'),
    path('new/', testapp.views.new, name='new'),
    path('new/create', testapp.views.create, name='create'),
    path('update/', testapp.views.update, name='update'),
    path('update/<int:num>', testapp.views.update, name="update"),
    path('delete/<int:num>', testapp.views.delete, name='delete'),
]

# path('경로/<자료형:변수이름>', views.함수, name='이름')