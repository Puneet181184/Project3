from django.conf.urls import url
from paragliding_app import views
from django.urls import re_path,path
app_name="paragliding_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'player/',views.player,name='player'),
  re_path(r'about/',views.about,name='about'),
  ]