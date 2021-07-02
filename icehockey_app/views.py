from django.shortcuts import render
from icehockey_app.models import icehockey_db
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"icehockey_app/home.html")
def player(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/player.html",context=icehockey_dict)		
def about(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/about.html",context=icehockey_dict)       
def details(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/details.html",context=icehockey_dict) 
def gamestats(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/gamestats.html",context=icehockey_dict)
def goalstats(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/goalstats.html",context=icehockey_dict)
def pointstats(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/pointstats.html",context=icehockey_dict)
def shotstats(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/shotstats.html",context=icehockey_dict)       











