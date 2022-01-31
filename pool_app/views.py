from django.shortcuts import render
from pool_app.models import pool_db
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"pool_app/home.html")
def player(request):
    players_list=pool_db.objects.order_by("name")
    pool_dict={"player":players_list}
    return render(request,"pool_app/player.html",context=pool_dict)		
def about(request):
    players_list=pool_db.objects.order_by("name")
    pool_dict={"player":players_list}
    return render(request,"pool_app/about.html",context=pool_dict)
def details(request):
    players_list=pool_db.objects.order_by("name")
    pool_dict={"player":players_list}
    return render(request,"pool_app/details.html",context=pool_dict)
def pointstats(request):
    players_list=pool_db.objects.order_by("name")
    pool_dict={"player":players_list}
    return render(request,"pool_app/pointstats.html",context=pool_dict)	
def careerstats(request):
    players_list=pool_db.objects.order_by("name")
    pool_dict={"player":players_list}
    return render(request,"pool_app/careerstats.html",context=pool_dict)		    	    		    		    