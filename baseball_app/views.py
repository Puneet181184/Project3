from django.shortcuts import render
from baseball_app.models import baseball_db


def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"baseball_app/home.html")
def player(request):
    players_list=baseball_db.objects.order_by("name")
    baseball_dict={"player":players_list}
    return render(request,"baseball_app/player.html",context=baseball_dict)			



