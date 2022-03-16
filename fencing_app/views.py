from django.shortcuts import render
from fencing_app.models import fencing_db
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"fencing_app/home.html")
def player(request):
    players_list=fencing_db.objects.order_by("name")
    fencing_dict={"player":players_list}
    return render(request,"fencing_app/player.html",context=fencing_dict)		