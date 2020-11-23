from django.conf.urls import url
from main import views
from django.urls import re_path,path
app_name="main"
urlpatterns=[
re_path(r'',views.main,name='main'),
  ]
  

