from django.conf.urls import url
from chess_app import views
from django.urls import re_path,path
app_name="chess_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'player/',views.player,name='player'),
  re_path(r'about/',views.about,name='about'),
  re_path(r'details/',views.details,name='details'),
  re_path(r'personalstats/',views.personalstats,name='personalstats'),
  re_path(r'ratingstats/',views.ratingstats,name='ratingstats'),
  re_path(r'gamestats/',views.gamestats,name='gamestats'),
  re_path(r'form_p/',views.form_player,name='form_player'),
  re_path(r'form_a/',views.form_about,name='form_about'),
  re_path(r'form_d/',views.form_details,name='form_details'),
  re_path(r'form_pe/',views.form_personalstats,name='form_personalstats'),
  re_path(r'form_r/',views.form_ratingstats,name='form_ratingstats'),
  re_path(r'form_g/',views.form_gamestats,name='form_gamestats'),

]  