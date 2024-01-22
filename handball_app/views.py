from django.shortcuts import render
from handball_app.models import handball_db
from handball_app.forms import playerform
from handball_app.forms import aboutform
from handball_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"handball_app/home.html")
def player(request):
    players_list=handball_db.objects.order_by("name")
    handball_dict={"player":players_list}
    return render(request,"handball_app/player.html",context=archery_dict)
def about(request):
    players_list=handball_db.objects.order_by("name")
    handball_dict={"player":players_list}
    return render(request,"handball_app/about.html",context=archery_dict)	    	