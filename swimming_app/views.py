from django.shortcuts import render
from swimming_app.models import swimming_db

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"swimming_app/home.html")
def player(request):
    players_list=swimming_db.objects.order_by("name")
    swimming_dict={"player":players_list}
    return render(request,"swimming_app/player.html",context=swimming_dict)		
def about(request):
    players_list=swimming_db.objects.order_by("name")
    swimming_dict={"player":players_list}
    return render(request,"swimming_app/about.html",context=swimming_dict)
def details(request):
    players_list=swimming_db.objects.order_by("name")
    swimming_dict={"player":players_list}
    return render(request,"swimming_app/details.html",context=swimming_dict)
def pointstats(request):
    players_list=swimming_db.objects.order_by("name")
    swimming_dict={"player":players_list}
    return render(request,"swimming_app/pointstats.html",context=swimming_dict)		    		    		    