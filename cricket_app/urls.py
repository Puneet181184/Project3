from django.conf.urls import url
from cricket_app import views
from django.urls import re_path,path
app_name="cricket_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'player/',views.player,name='player'),
  re_path(r'about/',views.about,name='about'),
  re_path(r'odistats/',views.odistats,name='odistats'),
  re_path(r'teststats/',views.teststats,name='teststats'),
  re_path(r't20stats/',views.t20stats,name='t20stats'),
  re_path(r'form_p/',views.form_player,name='form_player'),
  ]
  

