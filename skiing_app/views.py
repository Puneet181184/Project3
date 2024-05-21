from django.shortcuts import render
from skiing_app.models import skiing_db
from skiing_app.forms import playerform
from skiing_app.forms import aboutform
from skiing_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"skiing_app/home.html")
def player(request):
    players_list=skiing_db.objects.order_by("name")
    skiing_dict={"player":players_list}
    return render(request,"skiing_app/player.html",context=skiing_dict)		
def about(request):
    players_list=skiing_db.objects.order_by("name")
    skiing_dict={"player":players_list}
    return render(request,"skiing_app/about.html",context=skiing_dict)     