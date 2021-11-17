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
  re_path(r'form_a/',views.form_about,name='form_about'),
  re_path(r'form_d/',views.form_details,name='form_details'),
  re_path(r'form_c/',views.form_careerstats,name='form_careerstats'),
  re_path(r'form_m/',views.form_matchstats,name='form_matchstats'),
  re_path(r'form_t/',views.form_titlestats,name='form_titlestats'),
  re_path(r'search_p/',views.search_player,name='search_player'),
  ]