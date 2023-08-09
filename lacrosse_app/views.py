from django.shortcuts import render
from lacrosse_app.models import lacrosse_db
from lacrosse_app.forms import playerform
from lacrosse_app.forms import aboutform
from lacrosse_app.forms import pointstatsform
from lacrosse_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"lacrosse_app/home.html")
def player(request):
    players_list=lacrosse_db.objects.order_by("name")
    lacrosse_dict={"player":players_list}
    return render(request,"lacrosse_app/player.html",context=lacrosse_dict)		
def about(request):
    players_list=lacrosse_db.objects.order_by("name")
    lacrosse_dict={"player":players_list}
    return render(request,"lacrosse_app/about.html",context=lacrosse_dict)     
def player(request):
    players_list=lacrosse_db.objects.order_by("name")
    lacrosse_dict={"player":players_list}
    return render(request,"lacrosse_app/pointstats.html",context=lacrosse_dict)         