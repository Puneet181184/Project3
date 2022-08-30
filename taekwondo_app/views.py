from django.shortcuts import render
from taekwondo_app.models import taekwondo_db
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"taekwondo_app/home.html")
def player(request):
    players_list=taekwondo_db.objects.order_by("name")
    taekwondo_dict={"player":players_list}
    return render(request,"taekwondo_app/player.html",context=taekwondo_dict)	