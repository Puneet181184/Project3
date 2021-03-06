from django.conf.urls import url
from football_app import views
from django.urls import re_path,path
app_name="football_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'player/',views.player,name='player'),
  re_path(r'about/',views.about,name='about'),
  re_path(r'details/',views.details,name='details'),
  re_path(r'matchstats/',views.matchstats,name='matchstats'),
  re_path(r'goalstats/',views.goalstats,name='goalstats'),
  re_path(r'penaltystats/',views.penaltystats,name='penaltystats'),
  re_path(r'cardstats/',views.cardstats,name='cardstats'),
  re_path(r'form_p/',views.form_player,name='form_player'),
  re_path(r'form_a/',views.form_about,name='form_about'),
  re_path(r'form_d/',views.form_details,name='form_details'),
  re_path(r'form_m/',views.form_matchstats,name='form_matchstats'),
  re_path(r'form_g/',views.form_goalstats,name='form_goalstats'),
  re_path(r'form_pe/',views.form_penaltystats,name='form_penaltystats'),
  re_path(r'form_c/',views.form_cardstats,name='form_cardstats'),
  re_path(r'search_p/',views.search_player,name='search_player'),
  re_path(r'search_a/',views.search_about,name='search_about'),
  re_path(r'search_d/',views.search_details,name='search_details'),
  re_path(r'search_m/',views.search_matchstats,name='search_matchstats'),
  re_path(r'search_g/',views.search_goalstats,name='search_goalstats'),
  re_path(r'search_pe/',views.search_penaltystats,name='search_penaltystats'),
  re_path(r'search_c/',views.search_cardstats,name='search_cardstats'),
 ]
  

