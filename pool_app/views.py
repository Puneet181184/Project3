from django.shortcuts import render

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"pool_app/home.html")
def player(request):
    players_list=pool_db.objects.order_by("name")
    pool_dict={"player":players_list}
    return render(request,"pool_app/player.html",context=pool_dict)		