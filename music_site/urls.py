"""music_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path("music_app",include("music_app.urls")),
    path("books_app",include("books_app.urls")),
    path("home",include("main.urls")),
    path("cricket_app",include("cricket_app.urls")),
    path("football_app",include("football_app.urls")),
    path("tennis_app",include("tennis_app.urls")),
    path("chess_app",include("chess_app.urls")),
    path("basketball_app",include("basketball_app.urls")),
    path("baseball_app",include("baseball_app.urls")),
    path("rugby_app",include("rugby_app.urls")),
    path("icehockey_app",include("icehockey_app.urls")),
    path("golf_app",include("golf_app.urls")),
    path("badminton_app",include("badminton_app.urls")),
    path("tabletennis_app",include("tabletennis_app.urls")),
    path("bowling_app",include("bowling_app.urls")),
    path("weightlifting_app",include("weightlifting_app.urls")),
    path("pool_app",include("pool_app.urls")),
    path("archery_app",include("archery_app.urls")),
    path("fencing_app",include("fencing_app.urls")),
    path("cycling_app",include("cycling_app.urls")),
    path("darts_app",include("darts_app.urls")),
    path("karate_app",include("karate_app.urls")),
    path("surfing_app",include("surfing_app.urls")),
    path("taekwondo_app",include("taekwondo_app.urls")),
    path("volleyball_app",include("volleyball_app.urls")),
    path("horseracing_app",include("horseracing_app.urls")),
    path("judo_app",include("judo_app.urls")),
    path("swimmimg_app",include("swimming_app.urls")),
    path("kickboxing_app",include("kickboxing_app.urls")),
    path("rockclimbing_app",include("rockclimbing_app.urls")),
    path("iceskating_app",include("iceskating_app.urls")),
    path("curling_app",include("curling_app.urls")),
    path("lacrosse_app",include("lacrosse_app.urls")),
    path("rowing_app",include("rowing_app.urls")),
    path("polo_app",include("polo_app.urls")),
    path("handball_app",include("handball_app.urls")),
    path("boxing_app",include("boxing_app.urls")),
    path("skiing_app",include("skiing_app.urls")),
]
