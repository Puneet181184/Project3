from django.shortcuts import render
from judo_app.models import judo_db
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"judo_app/home.html")
def player(request):
    players_list=judo_db.objects.order_by("name")
    judo_dict={"player":players_list}
    return render(request,"judo_app/player.html",context=judo_dict)	
def about(request):
    players_list=judo_db.objects.order_by("name")
    judo_dict={"player":players_list}
    return render(request,"judo_app/about.html",context=judo_dict)	
def pointstats(request):
    players_list=judo_db.objects.order_by("name")
    judo_dict={"player":players_list}
    return render(request,"judo_app/pointstats.html",context=judo_dict)	        