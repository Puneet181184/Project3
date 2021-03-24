from django.shortcuts import render
from basketball_app.models import basketball_db

# Create your views here.
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"basketball_app/home.html")
def player(request):
    players_list=basketball_db.objects.order_by("name")
    basketball_dict={"player":players_list}
    return render(request,"basketball_app/player.html",context=basketball_dict)		
