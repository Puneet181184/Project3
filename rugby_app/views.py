from django.shortcuts import render
from rugby_app.models import rugby_db
# Create your views here.
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"rugby_app/home.html")
def player(request):
    players_list=rugby_db.objects.order_by("name")
    rugby_dict={"player":players_list}
    return render(request,"rugby_app/player.html",context=rugby_dict)			
	
