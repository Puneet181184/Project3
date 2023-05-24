from django.shortcuts import render
from iceskating_app.models import iceskating_db
from iceskating_app.forms import playerform
from iceskating_app.forms import aboutform
from iceskating_app.forms import detailsform
from archery_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"iceskating_app/home.html")
def player(request):
    players_list=iceskating_db.objects.order_by("name")
    iceskating_dict={"player":players_list}
    return render(request,"iceskating_app/player.html",context=iceskating_dict)			

