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
  re_path(r'form_p/',views.form_player,name='form_player'),
  re_path(r'form_a/',views.form_about,name='form_about'),
  re_path(r'form_d/',views.form_details,name='form_details'),
  re_path(r'form_c/',views.form_careerstats,name='form_careerstats'),
  re_path(r'form_po/',views.form_pointstats,name='form_pointstats'),
  re_path(r'form_w/',views.form_winstats,name='form_winstats'),
  re_path(r'form_g/',views.form_gamestats,name='form_gamestats'),


]
  


