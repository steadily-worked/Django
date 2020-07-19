from django.db import models

# Create your models here.
# Class 표이름(models.Model): -> '표이름'을 가진 표를 하나 만들고
#   필드명: models.데이터_형식() -> 표안에 필드(열)를 하나 만들고 그 필드의 데이터 형식을 정의
class Post(models.Model): # Post라는 제목을 가진 표를 만들것.
    title = models.CharField(max_length = 200)
    # title이라는 필드(열)를 만들고, 그 안의 데이터 형식은 Char, 즉 문자열로 생성할 건데,
    # 최대 길이(max_length)는 200인 것으로 설정할 것. (CharField는 max_length 설정이 필수임)
    pub_date = models.DateTimeField('date published')
    # pub_date라는 필드(열)를 만들고, 그 안에 데이터 형식은 DateTime, 즉 날짜와 시간 형식으로 생성할 것.
    body = models.TextField()
    # body 라는 필드(열)를 만들고, 그 안의 데이터 형식은 긴 문자열로 할 것.
