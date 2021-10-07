from django.shortcuts import render
from tabletennis_app.models import tabletennis_db
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"tabletennis_app/home.html")
def player(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/player.html",context=tabletennis_dict)			
def about(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/about.html",context=tabletennis_dict) 
def details(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/details.html",context=tabletennis_dict)
def careerstats(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/careerstats.html",context=tabletennis_dict) 
def singlesstats(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/singlesstats.html",context=tabletennis_dict)
def doublesstats(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/doublesstats.html",context=tabletennis_dict)
def totalstats(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/totalstats.html",context=tabletennis_dict)                                                      

