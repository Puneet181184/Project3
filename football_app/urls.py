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
  
  ]
  

