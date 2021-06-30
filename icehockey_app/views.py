from django.shortcuts import render
from icehockey_app.models import icehockey_db
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"icehockey_app/home.html")
def player(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/player.html",context=icehockey_dict)		

