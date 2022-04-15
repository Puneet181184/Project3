from django.shortcuts import render
from cycling_app.models import cycling_db
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"cycling_app/home.html")
def player(request):
    players_list=cycling_db.objects.order_by("name")
    cycling_dict={"player":players_list}
    return render(request,"cycling_app/player.html",context=cycling_dict)		
def about(request):
    players_list=cycling_db.objects.order_by("name")
    cycling_dict={"player":players_list}
    return render(request,"cycling_app/about.html",context=cycling_dict)		    
def details(request):
    players_list=cycling_db.objects.order_by("name")
    cycling_dict={"player":players_list}
    return render(request,"cycling_app/details.html",context=cycling_dict)		    
def gamestats(request):
    players_list=cycling_db.objects.order_by("name")
    cycling_dict={"player":players_list}
    return render(request,"cycling_app/gamestats.html",context=cycling_dict)	
def pointstats(request):
    players_list=cycling_db.objects.order_by("name")
    cycling_dict={"player":players_list}
    return render(request,"cycling_app/pointstats.html",context=cycling_dict)