from django.conf.urls import url
from books_app import views
from django.urls import re_path,path
app_name="books_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'book/',views.book,name='book'), 
  re_path(r'author/',views.author,name='author') 
  ]
  

