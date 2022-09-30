from django.shortcuts import render
from volleyball_app.models import volleyball_db
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"volleyball_app/home.html")
def player(request):
    players_list=volleyball_db.objects.order_by("name")
    volleyball_dict={"player":players_list}
    return render(request,"volleyball_app/player.html",context=volleyball_dict)	
def about(request):
    players_list=volleyball_db.objects.order_by("name")
    volleyball_dict={"player":players_list}
    return render(request,"volleyball_app/about.html",context=volleyball_dict)			
def details(request):
    players_list=volleyball_db.objects.order_by("name")
    volleyball_dict={"player":players_list}
    return render(request,"volleyball_app/details.html",context=volleyball_dict)	
def pointstats(request):
    players_list=volleyball_db.objects.order_by("name")
    volleyball_dict={"player":players_list}
    return render(request,"volleyball_app/pointstats.html",context=volleyball_dict)			


