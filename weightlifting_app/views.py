from django.shortcuts import render
from weightlifting_app.models import weightlifting_db
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"weightlifting_app/home.html")
def player(request):
    players_list=weightlifting_db.objects.order_by("name")
    weightlifting_dict={"player":players_list}
    return render(request,"weightlifting_app/player.html",context=weightlifting_dict)		
def about(request):
    players_list=weightlifting_db.objects.order_by("name")
    weightlifting_dict={"player":players_list}
    return render(request,"weightlifting_app/player.html",context=weightlifting_dict)       
def details(request):
    players_list=weightlifting_db.objects.order_by("name")
    weightlifting_dict={"player":players_list}
    return render(request,"weightlifting_app/player.html",context=weightlifting_dict)       
def careerstats(request):
    players_list=weightlifting_db.objects.order_by("name")
    weightlifting_dict={"player":players_list}
    return render(request,"weightlifting_app/player.html",context=weightlifting_dict)       
def matchstats(request):
    players_list=weightlifting_db.objects.order_by("name")
    weightlifting_dict={"player":players_list}
    return render(request,"weightlifting_app/player.html",context=weightlifting_dict)       
