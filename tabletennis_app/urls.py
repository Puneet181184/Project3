from django.conf.urls import url
from tabletennis_app import views
from django.urls import re_path,path
app_name="tabletennis_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'player/',views.player,name='player'),
  re_path(r'about/',views.about,name='about'),
  re_path(r'details/',views.details,name='details'),
  re_path(r'careerstats/',views.careerstats,name='careerstats'),
  re_path(r'singlesstats/',views.singlesstats,name='singlesstats'),
  re_path(r'doublesstats/',views.doublesstats,name='doublesstats'),
  re_path(r'totalstats/',views.totalstats,name='totalstats'),
  re_path(r'form_p/',views.form_player,name='form_player'),
  re_path(r'form_a/',views.form_about,name='form_about'),
  re_path(r'form_d/',views.form_details,name='form_details'),
  re_path(r'form_c/',views.form_careerstats,name='form_careerstats'),
  re_path(r'form_s/',views.form_singlesstats,name='form_singlesstats'),
  re_path(r'form_do/',views.form_doublesstats,name='form_doublesstats'),
  re_path(r'form_t/',views.form_totalstats,name='form_totalstats'),
  re_path(r'search_p/',views.search_player,name='search_player'),
  re_path(r'search_a/',views.search_about,name='search_about'),
  re_path(r'search_d/',views.search_details,name='search_details'),
  re_path(r'search_c/',views.search_careerstats,name='search_careerstats'),
  re_path(r'search_s/',views.search_singlesstats,name='search_singlesstats'),
  re_path(r'search_do/',views.search_doublesstats,name='search_doublesstats'),
  re_path(r'search_t/',views.search_totalstats,name='search_totalstats'),
  
  

 ]
