from django.shortcuts import render
from rowing_app.models import rowing_db
from rowing_app.forms import playerform
from rowing_app.forms import aboutform
from rowing_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"rowing_app/home.html")
def player(request):
    players_list=rowing_db.objects.order_by("name")
    rowing_dict={"player":players_list}
    return render(request,"rowing_app/player.html",context=rowing_dict)		
def about(request):
    players_list=rowing_db.objects.order_by("name")
    rowing_dict={"player":players_list}
    return render(request,"rowing_app/about.html",context=rowing_dict)     