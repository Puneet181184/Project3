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



]
