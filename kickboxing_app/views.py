from django.shortcuts import render
from kickboxing_app.models import kickboxing_db
from kickboxing_app.forms import playerform
from kickboxing_app.forms import aboutform
from kickboxing_app.forms import pointstatsform
from kickboxing_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"kickboxing_app/home.html")
def player(request):
    players_list=kickboxing_db.objects.order_by("name")
    kickboxing_dict={"player":players_list}
    return render(request,"kickboxing_app/player.html",context=kickboxing_dict)	
def about(request):
    players_list=kickboxing_db.objects.order_by("name")
    kickboxing_dict={"player":players_list}
    return render(request,"kickboxing_app/about.html",context=kickboxing_dict)	
def pointstats(request):
    players_list=kickboxing_db.objects.order_by("name")
    kickboxing_dict={"player":players_list}
    return render(request,"kickboxing_app/pointstats.html",context=kickboxing_dict)			    		    		

