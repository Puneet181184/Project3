from django.shortcuts import render
from chess_app.models import chess_db
# Create your views here.
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"chess_app/home.html")
def player(request):
    players_list=chess_db.objects.order_by("name")
    chess_dict={"player":players_list}
    return render(request,"chess_app/player.html",context=chess_dict)		
def about(request):
    players_list=chess_db.objects.order_by("name")
    chess_dict={"player":players_list}
    return render(request,"chess_app/about.html",context=chess_dict)		
def details(request):
    players_list=chess_db.objects.order_by("name")
    chess_dict={"player":players_list}
    return render(request,"chess_app/details.html",context=chess_dict)		
def personalstats(request):
    players_list=chess_db.objects.order_by("name")
    chess_dict={"player":players_list}
    return render(request,"chess_app/personalstats.html",context=chess_dict)		
def ratingstats(request):
    players_list=chess_db.objects.order_by("name")
    chess_dict={"player":players_list}
    return render(request,"chess_app/ratingstats.html",context=chess_dict)
def gamestats(request):
    players_list=chess_db.objects.order_by("name")
    chess_dict={"player":players_list}
    return render(request,"chess_app/gamestats.html",context=chess_dict)	    		
