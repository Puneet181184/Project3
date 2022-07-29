from django.shortcuts import render
from surfing_app.models import surfing_db
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"surfing_app/home.html")
def player(request):
    players_list=surfing_db.objects.order_by("name")
    surfing_dict={"player":players_list}
    return render(request,"surfing_app/player.html",context=surfing_dict)	
def about(request):
    players_list=surfing_db.objects.order_by("name")
    surfing_dict={"about":players_list}
    return render(request,"surfing_app/about.html",context=surfing_dict) 
def details(request):
    players_list=surfing_db.objects.order_by("name")
    surfing_dict={"details":players_list}
    return render(request,"surfing_app/details.html",context=surfing_dict) 
def pointstats(request):
    players_list=surfing_db.objects.order_by("name")
    surfing_dict={"pointstats":players_list}
    return render(request,"surfing_app/pointstats.html",context=surfing_dict)          
