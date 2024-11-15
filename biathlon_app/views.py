from django.shortcuts import render
from biathlon_app.models import biathlon_db
from biathlon_app.forms import playerform
from biathlon_app.forms import aboutform
from biathlon_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"biathlon_app/home.html")
def player(request):
    players_list=biathlon_db.objects.order_by("name")
    biathlon_dict={"player":players_list}
    return render(request,"biathlon_app/player.html",context=biathlon_dict)		
def about(request):
    players_list=biathlon_db.objects.order_by("name")
    biathlon_dict={"player":players_list}
    return render(request,"biathlon_app/about.html",context=biathlon_dict)	