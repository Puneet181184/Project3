from django.conf.urls import url
from lacrosse_app import views
from django.urls import re_path,path
app_name="lacrosse_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'player/',views.player,name='player'),
  re_path(r'about/',views.about,name='about'),
  re_path(r'pointstats/',views.pointstats,name='pointstats'),
  re_path(r'form_p/',views.form_player,name='form_player'),
  re_path(r'form_a/',views.form_about,name='form_about'),
  re_path(r'form_po/',views.form_pointstats,name='form_pointstats'),
  ]