from django.conf.urls import url
from tennis_app import views
from django.urls import re_path,path
app_name="tennis_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'player/',views.player,name='player'),
  re_path(r'about/',views.about,name='about'),
  re_path(r'details/',views.details,name='details'),
  re_path(r'careerstats/',views.careerstats,name='careerstats'),
  re_path(r'pointstats/',views.pointstats,name='pointstats'),
  re_path(r'winstats/',views.winstats,name='winstats'),
  re_path(r'gamestats/',views.gamestats,name='gamestats'),


 ]
  


