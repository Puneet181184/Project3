from django.conf.urls import url
from pool_app import views
from django.urls import re_path,path
app_name="pool_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'player/',views.player,name='player'),
  ]