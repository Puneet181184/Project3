from django.shortcuts import render
from tennis_app.models import tennis_db
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"tennis_app/home.html")
def player(request):
    players_list=tennis_db.objects.order_by("name")
    tennis_dict={"player":players_list}
    return render(request,"tennis_app/player.html",context=tennis_dict)		
