from django.shortcuts import render
from horseracing_app.models import horseracing_db

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"horseracing_app/home.html")
def player(request):
    players_list=horseracing_db.objects.order_by("name")
    horseracing_dict={"player":players_list}
    return render(request,"horseracing_app/player.html",context=horseracing_dict)		