from django.shortcuts import render
from curling_app.models import curling_db
from curling_app.forms import playerform
from curling_app.forms import aboutform
from curling_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"curling_app/home.html")
def player(request):
    players_list=curling_db.objects.order_by("name")
    curling_dict={"player":players_list}
    return render(request,"curling_app/player.html",context=curling_dict)
def about(request):
    players_list=curling_db.objects.order_by("name")
    curling_dict={"player":players_list}
    return render(request,"curling_app/about.html",context=curling_dict)    