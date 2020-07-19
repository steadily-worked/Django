from django.contrib import admin
from .models import Post # 같은 폴더 위치에 있는 models라는 파일에, Post라는 표를 가져오라는 뜻.

# Register your models here.
admin.site.register(Post) # 'admin' 이라는 site에 Post라는 표를 등록해라 라는 뜻