from django.conf.urls import url
from badminton_app import views
from django.urls import re_path,path
app_name="badminton_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'player/',views.player,name='player'),
  re_path(r'about/',views.about,name='about'),
  re_path(r'details/',views.details,name='details'),
  re_path(r'careerstats/',views.careerstats,name='careerstats'),
  re_path(r'singlesstats/',views.singlesstats,name='singlesstats'),
  re_path(r'doublesstats/',views.doublesstats,name='doublesstats'),
  re_path(r'mixedstats/',views.mixedstats,name='mixedstats'),
  re_path(r'form_p/',views.form_player,name='form_player'),
  re_path(r'form_a/',views.form_about,name='form_about'),
  re_path(r'form_d/',views.form_details,name='form_details'),
  re_path(r'form_c/',views.form_careerstats,name='form_careerstats'),
  re_path(r'form_s/',views.form_singlesstats,name='form_singlesstats'),
  re_path(r'form_do/',views.form_doublesstats,name='form_doublesstats'),
  re_path(r'form_m/',views.form_mixedstats,name='form_mixedstats'),
 ]

