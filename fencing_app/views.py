from django.shortcuts import render
from fencing_app.models import fencing_db
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"fencing_app/home.html")
def player(request):
    players_list=fencing_db.objects.order_by("name")
    fencing_dict={"player":players_list}
    return render(request,"fencing_app/player.html",context=fencing_dict)		
def about(request):
    players_list=fencing_db.objects.order_by("name")
    fencing_dict={"player":players_list}
    return render(request,"fencing_app/about.html",context=fencing_dict)
def details(request):
    players_list=fencing_db.objects.order_by("name")
    fencing_dict={"player":players_list}
    return render(request,"fencing_app/details.html",context=fencing_dict)	
def gamestats(request):
    players_list=fencing_db.objects.order_by("name")
    fencing_dict={"player":players_list}
    return render(request,"fencing_app/gamestats.html",context=fencing_dict)
def pointstats(request):
    players_list=fencing_db.objects.order_by("name")
    fencing_dict={"player":players_list}
    return render(request,"fencing_app/pointstats.html",context=fencing_dict)		    		    	    
