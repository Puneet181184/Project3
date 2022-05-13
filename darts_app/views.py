from django.shortcuts import render

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"darts_app/home.html")
def player(request):
    players_list=darts_db.objects.order_by("name")
    darts_dict={"player":players_list}
    return render(request,"darts_app/player.html",context=darts_dict)	