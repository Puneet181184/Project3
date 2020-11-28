from django.conf.urls import url
from cricket_app import views
from django.urls import re_path,path
app_name="cricket_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  ]
  

