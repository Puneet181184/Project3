from django.shortcuts import render
from skating_app.models import skating_db
from skating_app.forms import playerform
from skating_app.forms import aboutform
from skating_app.forms import searchform

# Create your views here.
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"skating_app/home.html")
def player(request):
    players_list=skating_db.objects.order_by("name")
    skating_dict={"player":players_list}
    return render(request,"skating_app/player.html",context=skating_dict)			
def about(request):
    players_list=skating_db.objects.order_by("name")
    skating_dict={"player":players_list}
    return render(request,"skating_app/about.html",context=skating_dict)	