from django.shortcuts import render
from surfing_app.models import surfing_db
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"surfing_app/home.html")
def player(request):
    players_list=surfing_db.objects.order_by("name")
    surfing_dict={"player":players_list}
    return render(request,"surfing_app/player.html",context=surfing_dict)	