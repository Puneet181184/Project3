from django.shortcuts import render
from baseball_app.models import baseball_db


def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"baseball_app/home.html")
def player(request):
    players_list=baseball_db.objects.order_by("name")
    baseball_dict={"player":players_list}
    return render(request,"baseball_app/player.html",context=baseball_dict)			
def about(request):
    players_list=baseball_db.objects.order_by("name")
    baseball_dict={"player":players_list}
    return render(request,"baseball_app/about.html",context=baseball_dict)
def details(request):
    players_list=baseball_db.objects.order_by("name")
    baseball_dict={"player":players_list}
    return render(request,"baseball_app/details.html",context=baseball_dict)
def gamestats(request):
    players_list=baseball_db.objects.order_by("name")
    baseball_dict={"player":players_list}
    return render(request,"baseball_app/gamestats.html",context=baseball_dict)
def runstats(request):
    players_list=baseball_db.objects.order_by("name")
    baseball_dict={"player":players_list}
    return render(request,"baseball_app/runstats.html",context=baseball_dict)
def strikestats(request):
    players_list=baseball_db.objects.order_by("name")
    baseball_dict={"player":players_list}
    return render(request,"baseball_app/strikestats.html",context=baseball_dict)
def basestats(request):
    players_list=baseball_db.objects.order_by("name")
    baseball_dict={"player":players_list}
    return render(request,"baseball_app/basestats.html",context=baseball_dict)
    		    		    		    		    		    		


