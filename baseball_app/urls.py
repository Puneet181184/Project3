from django.conf.urls import url
from baseball_app import views
from django.urls import re_path,path
app_name="baseball_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'player/',views.player,name='player'),
  re_path(r'about/',views.about,name='about'),
  re_path(r'details/',views.details,name='details'),
  re_path(r'gamestats/',views.gamestats,name='gamestats'),
  re_path(r'runstats/',views.runstats,name='runstats'),
  re_path(r'strikestats/',views.strikestats,name='strikestats'),
  re_path(r'basestats/',views.basestats,name='basestats'),
  re_path(r'form_p/',views.form_player,name='form_player'),
  
  
  
  
  
  
  
  ]