from django.shortcuts import render
from chess_app.models import chess_db
from chess_app.forms import playerform
from chess_app.forms import aboutform
from chess_app.forms import detailsform
from chess_app.forms import personalstatsform
from chess_app.forms import ratingstatsform
from chess_app.forms import gamestatsform
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

def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         dob=form.cleaned_data["dob"]
         nationality=form.cleaned_data["nationality"]
         defaults={"age":age,"dob":dob,"nationality":nationality}
         obj,created=chess_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"chess_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"chess_app/form_player.html",{"form":form})  
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         rank=form.cleaned_data["rank"]
         debut=form.cleaned_data["debut"]
         defaults={"rank":rank,"debut":debut}
         obj,created=chess_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"chess_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"chess_app/form_about.html",{"form":form})  
def form_details(request):
    form=detailsform()
    if request.method=="POST":
      form=detailsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         height=form.cleaned_data["height"]
         weight=form.cleaned_data["weight"]
         defaults={"height":height,"weight":weight}
         obj,created=chess_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"chess_app/submit_details.html")
      else:
         print("error form invalid")      
    return render(request,"chess_app/form_details.html",{"form":form}) 
def form_personalstats(request):
    form=personalstatsform()
    if request.method=="POST":
      form=personalstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         title=form.cleaned_data["title"]
         playerid=form.cleaned_data["playerid"]
         gender=form.cleaned_data["gender"]
         defaults={"title":title,"playerid":playerid,"gender":gender}
         obj,created=chess_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"chess_app/submit_personalstats.html")
      else:
         print("error form invalid")      
    return render(request,"chess_app/form_personalstats.html",{"form":form}) 
def form_ratingstats(request):
    form=ratingstatsform()
    if request.method=="POST":
      form=ratingstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         stdrating=form.cleaned_data["stdrating"]
         rapidrating=form.cleaned_data["rapidrating"]
         blitzrating=form.cleaned_data["blitzrating"]
         defaults={"stdrating":stdrating,"rapidrating":rapidrating,"blitzrating":blitzrating}
         obj,created=chess_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"chess_app/submit_ratingstats.html")
      else:
         print("error form invalid")      
    return render(request,"chess_app/form_ratingstats.html",{"form":form}) 
def form_gamestats(request):
    form=gamestatsform()
    if request.method=="POST":
      form=gamestatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         games=form.cleaned_data["games"]
         wins=form.cleaned_data["wins"]
         draws=form.cleaned_data["draws"]
         losses=form.cleaned_data["losses"]
         score=form.cleaned_data["score"]
         defaults={"games":games,"wins":wins,"draws":draws,"losses":losses,"score":score}
         obj,created=chess_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"chess_app/submit_gamestats.html")
      else:
         print("error form invalid")      
    return render(request,"chess_app/form_gamestats.html",{"form":form})                 	    		
