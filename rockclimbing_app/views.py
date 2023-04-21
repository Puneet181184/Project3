from django.shortcuts import render
from rockclimbing_app.models import rockclimbing_db
from rockclimbing_app.forms import playerform
from rockclimbing_app.forms import aboutform
from rockclimbing_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"rockclimbing_app/home.html")
def player(request):
    players_list=rockclimbing_db.objects.order_by("name")
    rockclimbing_dict={"player":players_list}
    return render(request,"rockclimbing_app/player.html",context=rockclimbing_dict)
def about(request):
    players_list=rockclimbing_db.objects.order_by("name")
    rockclimbing_dict={"player":players_list}
    return render(request,"rockclimbing_app/about.html",context=rockclimbing_dict)       
def pointstats(request):
    players_list=rockclimbing_db.objects.order_by("name")
    rockclimbing_dict={"player":players_list}
    return render(request,"rockclimbing_app/pointstats.html",context=rockclimbing_dict)    