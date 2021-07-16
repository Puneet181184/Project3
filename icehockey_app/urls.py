from django.conf.urls import url
from icehockey_app import views
from django.urls import re_path,path
app_name="icehockey_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'player/',views.player,name='player'),
  re_path(r'about/',views.about,name='about'),
  re_path(r'details/',views.details,name='details'),
  re_path(r'gamestats/',views.gamestats,name='gamestats'),
  re_path(r'goalstats/',views.goalstats,name='goalstats'),
  re_path(r'pointstats/',views.pointstats,name='pointstats'),
  re_path(r'shotstats/',views.shotstats,name='shotstats'),
  re_path(r'form_p/',views.form_player,name='form_player'),
  re_path(r'form_a/',views.form_about,name='form_about'),
  re_path(r'form_d/',views.form_details,name='form_details'),
  re_path(r'form_g/',views.form_gamestats,name='form_gamestats'),
  re_path(r'form_go/',views.form_goalstats,name='form_goalstats'),
  re_path(r'form_po/',views.form_pointstats,name='form_pointstats'),
  re_path(r'form_s/',views.form_shotstats,name='form_shotstats'),
  re_path(r'search_p/',views.search_player,name='search_player'),
  re_path(r'search_a/',views.search_about,name='search_about'),
  re_path(r'search_d/',views.search_details,name='search_details'),
  re_path(r'search_g/',views.search_gamestats,name='search_gamestats'),
  re_path(r'search_go/',views.search_goalstats,name='search_goalstats'),
  re_path(r'search_po/',views.search_pointstats,name='search_pointstats'),
  re_path(r'search_s/',views.search_shotstats,name='search_shotstats'),

]