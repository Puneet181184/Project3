from django.conf.urls import url
from cricket_app import views
from django.urls import re_path,path
app_name="cricket_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'player/',views.player,name='player'),
  re_path(r'about/',views.about,name='about'),
  re_path(r'odistats/',views.odistats,name='odistats'),
  re_path(r'teststats/',views.teststats,name='teststats'),
  re_path(r't20stats/',views.t20stats,name='t20stats'),
  re_path(r'form_p/',views.form_player,name='form_player'),
  re_path(r'form_a/',views.form_about,name='form_about'),
  re_path(r'form_o/',views.form_odistats,name='form_odistats'),
  re_path(r'form_t/',views.form_teststats,name='form_teststats'),
  re_path(r'form_t20/',views.form_t20stats,name='form_t20stats'),
  re_path(r'search_p/',views.search_player,name='search_player'),
  re_path(r'search_a/',views.search_about,name='search_about'),
  re_path(r'search_o/',views.search_odistats,name='search_odistats'),
  re_path(r'search_t/',views.search_teststats,name='search_teststats'),
  re_path(r'search_t20/',views.search_t20stats,name='search_t20stats'),
  ]
  

