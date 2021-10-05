from django.shortcuts import render
from tabletennis_app.models import tabletennis_db
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"tabletennis_app/home.html")
def player(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/player.html",context=tabletennis_dict)			
