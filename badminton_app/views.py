from django.shortcuts import render
from badminton_app.models import badminton_db
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"badminton_app/home.html")
def player(request):
    players_list=badminton_db.objects.order_by("name")
    badminton_dict={"player":players_list}
    return render(request,"badminton_app/player.html",context=badminton_dict)		
def about(request):
    players_list=badminton_db.objects.order_by("name")
    badminton_dict={"player":players_list}
    return render(request,"badminton_app/about.html",context=badminton_dict)
def details(request):
    players_list=badminton_db.objects.order_by("name")
    badminton_dict={"player":players_list}
    return render(request,"badminton_app/details.html",context=badminton_dict)
def careerstats(request):
    players_list=badminton_db.objects.order_by("name")
    badminton_dict={"player":players_list}
    return render(request,"badminton_app/careerstats.html",context=badminton_dict)
def singlesstats(request):
    players_list=badminton_db.objects.order_by("name")
    badminton_dict={"player":players_list}
    return render(request,"badminton_app/singlesstats.html",context=badminton_dict) 
def doublesstats(request):
    players_list=badminton_db.objects.order_by("name")
    badminton_dict={"player":players_list}
    return render(request,"badminton_app/doublesstats.html",context=badminton_dict)
def mixedstats(request):
    players_list=badminton_db.objects.order_by("name")
    badminton_dict={"player":players_list}
    return render(request,"badminton_app/mixedstats.html",context=badminton_dict)               