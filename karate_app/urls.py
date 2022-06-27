from django.conf.urls import url
from karate_app import views
from django.urls import re_path,path
app_name="karate_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'player/',views.player,name='player'),
  re_path(r'about/',views.about,name='about'),
  re_path(r'details/',views.details,name='details'),
  re_path(r'pointstats/',views.pointstats,name='pointstats'),
  re_path(r'form_p/',views.form_player,name='form_player'),
  ]