from django.shortcuts import render
from darts_app.models import darts_db

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"darts_app/home.html")
def player(request):
    players_list=darts_db.objects.order_by("name")
    darts_dict={"player":players_list}
    return render(request,"darts_app/player.html",context=darts_dict)
def about(request):
    players_list=darts_db.objects.order_by("name")
    darts_dict={"player":players_list}
    return render(request,"darts_app/about.html",context=darts_dict)
def details(request):
    players_list=darts_db.objects.order_by("name")
    darts_dict={"player":players_list}
    return render(request,"darts_app/details.html",context=darts_dict)	    	    
def gamestats(request):
    players_list=darts_db.objects.order_by("name")
    darts_dict={"player":players_list}
    return render(request,"darts_app/gamestats.html",context=darts_dict)
def pointstats(request):
    players_list=darts_db.objects.order_by("name")
    darts_dict={"player":players_list}
    return render(request,"darts_app/pointstats.html",context=darts_dict)	    	    