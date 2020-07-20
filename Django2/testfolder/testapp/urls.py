from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
	path('update/<int:num>', views.update, name='update'),
	path('delete/<int:num>', views.delete, name='delete'),
	path('album/', views.album, name='album')
]