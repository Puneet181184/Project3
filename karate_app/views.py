from django.shortcuts import render
from karate_app.models import karate_db

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"karate_app/home.html")
def player(request):
    players_list=karate_db.objects.order_by("name")
    karate_dict={"player":players_list}
    return render(request,"karate_app/player.html",context=karate_dict)		