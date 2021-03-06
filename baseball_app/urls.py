from django.conf.urls import url
from baseball_app import views
from django.urls import re_path,path
app_name="baseball_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'player/',views.player,name='player'),
  re_path(r'about/',views.about,name='about'),
  re_path(r'details/',views.details,name='details'),
  re_path(r'gamestats/',views.gamestats,name='gamestats'),
  re_path(r'runstats/',views.runstats,name='runstats'),
  re_path(r'strikestats/',views.strikestats,name='strikestats'),
  re_path(r'basestats/',views.basestats,name='basestats'),
  re_path(r'form_p/',views.form_player,name='form_player'),
  re_path(r'form_a/',views.form_about,name='form_about'),
  re_path(r'form_d/',views.form_details,name='form_details'),
  re_path(r'form_g/',views.form_gamestats,name='form_gamestats'),
  re_path(r'form_r/',views.form_runstats,name='form_runstats'),
  re_path(r'form_s/',views.form_strikestats,name='form_strikestats'),
  re_path(r'form_b/',views.form_basestats,name='form_basestats'),
  re_path(r'search_p/',views.search_player,name='search_player'),
  re_path(r'search_a/',views.search_about,name='search_about'),
  re_path(r'search_d/',views.search_details,name='search_details'),
  re_path(r'search_g/',views.search_gamestats,name='search_gamestats'),
  re_path(r'search_r/',views.search_runstats,name='search_runstats'),
  re_path(r'search_s/',views.search_strikestats,name='search_strikestats'),
  re_path(r'search_b/',views.search_basestats,name='search_basestats'),
]