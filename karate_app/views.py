from django.shortcuts import render
from karate_app.models import karate_db

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"karate_app/home.html")
def player(request):
    players_list=karate_db.objects.order_by("name")
    karate_dict={"player":players_list}
    return render(request,"karate_app/player.html",context=karate_dict)		
def about(request):
    players_list=karate_db.objects.order_by("name")
    karate_dict={"player":players_list}
    return render(request,"karate_app/about.html",context=karate_dict)	
def details(request):
    players_list=karate_db.objects.order_by("name")
    karate_dict={"player":players_list}
    return render(request,"karate_app/details.html",context=karate_dict)
def pointstats(request):
    players_list=karate_db.objects.order_by("name")
    karate_dict={"player":players_list}
    return render(request,"karate_app/pointstats.html",context=karate_dict)		    		    	    