from django.shortcuts import render
from archery_app.models import archery_db
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"archery_app/home.html")
def player(request):
    players_list=archery_db.objects.order_by("name")
    archery_dict={"player":players_list}
    return render(request,"archery_app/player.html",context=archery_dict)		