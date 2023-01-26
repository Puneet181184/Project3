from django.shortcuts import render
from swimming_app.models import swimming_db

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"swimming_app/home.html")
def player(request):
    players_list=swimming_db.objects.order_by("name")
    swimming_dict={"player":players_list}
    return render(request,"swimming_app/player.html",context=swimming_dict)		