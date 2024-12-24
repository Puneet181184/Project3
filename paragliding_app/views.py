from django.shortcuts import render
from paragliding_app.models import paragliding_db
from paragliding_app.forms import playerform
from paragliding_app.forms import aboutform
from paragliding_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"paragliding_app/home.html")
def player(request):
    players_list=paragliding_db.objects.order_by("name")
    paragliding_dict={"player":players_list}
    return render(request,"paragliding_app/player.html",context=paragliding_dict)		
def about(request):
    players_list=paragliding_db.objects.order_by("name")
    paragliding_dict={"player":players_list}
    return render(request,"paragliding_app/about.html",context=paragliding_dict)  