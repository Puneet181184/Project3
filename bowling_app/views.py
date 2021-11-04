from django.shortcuts import render

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"bowling_app/home.html")
def player(request):
    players_list=bowling_db.objects.order_by("name")
    bowling_dict={"player":players_list}
    return render(request,"bowling_app/player.html",context=bowling_dict)		
