from django.conf.urls import url
from bowling_app import views
from django.urls import re_path,path
app_name="bowling_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'player/',views.player,name='player'),
  re_path(r'about/',views.about,name='about'),
  re_path(r'details/',views.details,name='details'),
  re_path(r'careerstats/',views.careerstats,name='careerstats'),
  re_path(r'matchstats/',views.matchstats,name='matchstats'),
  re_path(r'titlestats/',views.titlestats,name='titlestats'),
  re_path(r'form_p/',views.form_player,name='form_player'),
  ]