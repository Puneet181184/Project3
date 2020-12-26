from django.conf.urls import url
from football_app import views
from django.urls import re_path,path
app_name="football_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  
  ]
  

