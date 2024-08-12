from django.shortcuts import render
from diving_app.models import diving_db
from diving_app.forms import playerform
from diving_app.forms import aboutform
from diving_app.forms import searchform
# Create your views here.
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"diving_app/home.html")
def player(request):
    players_list=diving_db.objects.order_by("name")
    diving_dict={"player":players_list}
    return render(request,"diving_app/player.html",context=diving_dict)		
def about(request):
    players_list=diving_db.objects.order_by("name")
    diving_dict={"player":players_list}
    return render(request,"diving_app/about.html",context=diving_dict)	