from django.shortcuts import render
from hockey_app.models import hockey_db
from hockey_app.forms import playerform
from hockey_app.forms import aboutform
from hockey_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"hockey_app/home.html")
def player(request):
    players_list=hockey_db.objects.order_by("name")
    hockey_dict={"player":players_list}
    return render(request,"hockey_app/player.html",context=hockey_dict)		
def about(request):
    players_list=hockey_db.objects.order_by("name")
    hockey_dict={"player":players_list}
    return render(request,"hockey_app/about.html",context=hockey_dict)		
