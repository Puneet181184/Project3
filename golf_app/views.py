from django.shortcuts import render
from golf_app.models import golf_db

# Create your views here.
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"golf_app/home.html")
def player(request):
    players_list=golf_db.objects.order_by("name")
    golf_dict={"player":players_list}
    return render(request,"golf_app/player.html",context=golf_dict)			
def about(request):
    players_list=golf_db.objects.order_by("name")
    golf_dict={"player":players_list}
    return render(request,"golf_app/about.html",context=golf_dict)     
def details(request):
    players_list=golf_db.objects.order_by("name")
    golf_dict={"player":players_list}
    return render(request,"golf_app/details.html",context=golf_dict)
def gamestats(request):
    players_list=golf_db.objects.order_by("name")
    golf_dict={"player":players_list}
    return render(request,"golf_app/gamestats.html",context=golf_dict) 
def positionstats(request):
    players_list=golf_db.objects.order_by("name")
    golf_dict={"player":players_list}
    return render(request,"golf_app/positionstats.html",context=golf_dict) 
def pointstats(request):
    players_list=golf_db.objects.order_by("name")
    golf_dict={"player":players_list}
    return render(request,"golf_app/pointstats.html",context=golf_dict)                                  