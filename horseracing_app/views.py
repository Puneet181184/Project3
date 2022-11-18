from django.shortcuts import render
from horseracing_app.models import horseracing_db

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"horseracing_app/home.html")
def player(request):
    players_list=horseracing_db.objects.order_by("name")
    horseracing_dict={"player":players_list}
    return render(request,"horseracing_app/player.html",context=horseracing_dict)		
def about(request):
    players_list=horseracing_db.objects.order_by("name")
    horseracing_dict={"player":players_list}
    return render(request,"horseracing_app/about.html",context=horseracing_dict)
def details(request):
    players_list=horseracing_db.objects.order_by("name")
    horseracing_dict={"player":players_list}
    return render(request,"horseracing_app/details.html",context=horseracing_dict)		    		    
def pointstats(request):
    players_list=horseracing_db.objects.order_by("name")
    horseracing_dict={"player":players_list}
    return render(request,"horseracing_app/pointstats.html",context=horseracing_dict)		    