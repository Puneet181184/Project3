from django.shortcuts import render
from golf_app.models import golf_db

# Create your views here.
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"golf_app/home.html")
def player(request):
    players_list=golf_db.objects.order_by("name")
    golf_dict={"player":players_list}
    return render(request,"golf_app/player.html",context=golf_dict)			
