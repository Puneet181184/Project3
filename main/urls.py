from django.conf.urls import url
from main import views
from django.urls import re_path,path
app_name="main"
urlpatterns=[
re_path(r'home',views.main,name='main'),
re_path(r'contactus',views.contactus,name="contactus")
  ]
  

