from django.conf.urls import url
from chess_app import views
from django.urls import re_path,path
app_name="chess_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'player/',views.player,name='player'),
]  