from django.conf.urls import url
from tabletennis_app import views
from django.urls import re_path,path
app_name="tabletennis_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'player/',views.player,name='player'),
  re_path(r'about/',views.about,name='about'),
  re_path(r'details/',views.details,name='details'),
  re_path(r'careerstats/',views.careerstats,name='careerstats'),
  re_path(r'singlesstats/',views.singlesstats,name='singlesstats'),
  re_path(r'doublesstats/',views.doublesstats,name='doublesstats'),
  re_path(r'totalstats/',views.totalstats,name='totalstats'),
  re_path(r'form_p/',views.form_player,name='form_player'),
  





  ]
