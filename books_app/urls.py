from django.conf.urls import url
from books_app import views
from django.urls import re_path,path
app_name="books_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'book/',views.book,name='book'), 
  re_path(r'author/',views.author,name='author'), 
  re_path(r'codes/',views.codes,name='codes'),
  re_path(r'other/',views.other,name='other'),
  re_path(r'form_b/',views.form_book,name='form_book'),
  re_path(r'form_a/',views.form_author,name='form_author'),
  re_path(r'form_c/',views.form_codes,name='form_codes'),
  re_path(r'form_o/',views.form_other,name='form_other'),
  re_path(r'search_b/',views.search_book,name='search_book'),
  ]
  

