from django.conf.urls import url
from chess_app import views
from django.urls import re_path,path
app_name="chess_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'player/',views.player,name='player'),
  re_path(r'about/',views.about,name='about'),
  re_path(r'details/',views.details,name='details'),
  re_path(r'personalstats/',views.personalstats,name='personalstats'),
  re_path(r'ratingstats/',views.ratingstats,name='ratingstats'),
  re_path(r'gamestats/',views.gamestats,name='gamestats'),

  


]  