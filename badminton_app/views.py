from django.shortcuts import render
from badminton_app.models import badminton_db
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"badminton_app/home.html")
def player(request):
    players_list=badminton_db.objects.order_by("name")
    badminton_dict={"player":players_list}
    return render(request,"badminton_app/player.html",context=badminton_dict)		

