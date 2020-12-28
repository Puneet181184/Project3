from django.shortcuts import render


def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"football_app/home.html")
def player(request):
    players_list=football_db.objects.order_by("name")
    football_dict={"player":players_list}
    return render(request,"football_app/player.html",context=football_dict)		

