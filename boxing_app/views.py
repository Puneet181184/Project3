from django.shortcuts import render
from boxing_app.models import boxing_db
from boxing_app.forms import playerform
from boxing_app.forms import aboutform
from boxing_app.forms import pointstatsform
from boxing_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"boxing_app/home.html")
def player(request):
    players_list=boxing_db.objects.order_by("name")
    boxing_dict={"player":players_list}
    return render(request,"boxing_app/player.html",context=boxing_dict)			
def about(request):
    players_list=boxing_db.objects.order_by("name")
    boxing_dict={"player":players_list}
    return render(request,"boxing_app/about.html",context=boxing_dict)		
def pointstats(request):
    players_list=boxing_db.objects.order_by("name")
    boxing_dict={"player":players_list}
    return render(request,"boxing_app/pointstats.html",context=boxing_dict)		