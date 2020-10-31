from django.conf.urls import url
from music_app import views
from django.urls import re_path,path
app_name="music_app"
urlpatterns=[
  re_path(r'home/',views.home,name='home'),
  re_path(r'track/',views.track,name='track'),
  url('artist/',views.artist,name='artist'),
  url('codes/',views.codes,name='codes'),
  url('sesac/',views.sesac,name='sesac'),
  url('ascap/',views.ascap,name='ascap'),
  url('bmi/',views.bmi,name='bmi'),
  url('gmr/',views.gmr,name='gmr'),
 # url('form_music/',views.form_music,name='form_music'),
  url('form_t/',views.form_track,name='form_track'),
  url('form_a/',views.form_artist,name='form_artist'),
  url('form_c/',views.form_codes,name='form_codes'),
  url('form_s/',views.form_sesac,name='form_sesac'),
  url('form_p/',views.form_ascap,name='form_ascap'),
  url('form_b/',views.form_bmi,name='form_bmi'),
  url('form_g/',views.form_gmr,name='form_gmr'),
  url('search_t/',views.search_track,name='search_track'),
  url('search_a/',views.search_artist,name='search_artist'),
  url('search_p/',views.search_ascap,name='search_ascap'),
  url('search_b/',views.search_bmi,name='search_bmi'),
  url('search_c',views.search_codes,name='search_codes'),
  url('search_g',views.search_gmr,name='search_gmr'),
  url('search_s',views.search_sesac,name='search_sesac'),
  ]
  

