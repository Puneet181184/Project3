from django.conf.urls import url
from golf_app import views
from django.urls import re_path,path
app_name="golf_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'player/',views.player,name='player'),
  
 ] 