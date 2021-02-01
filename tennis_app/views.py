from django.shortcuts import render
from tennis_app.models import tennis_db
from football_app.forms import playerform
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"tennis_app/home.html")
def player(request):
    players_list=tennis_db.objects.order_by("name")
    tennis_dict={"player":players_list}
    return render(request,"tennis_app/player.html",context=tennis_dict)		
def about(request):
    players_list=tennis_db.objects.order_by("name")
    tennis_dict={"player":players_list}
    return render(request,"tennis_app/about.html",context=tennis_dict)
def details(request):
    players_list=tennis_db.objects.order_by("name")
    tennis_dict={"player":players_list}
    return render(request,"tennis_app/details.html",context=tennis_dict)
def careerstats(request):
    players_list=tennis_db.objects.order_by("name")
    tennis_dict={"player":players_list}
    return render(request,"tennis_app/careerstats.html",context=tennis_dict)
def pointstats(request):
    players_list=tennis_db.objects.order_by("name")
    tennis_dict={"player":players_list}
    return render(request,"tennis_app/pointstats.html",context=tennis_dict)		
def winstats(request):
    players_list=tennis_db.objects.order_by("name")
    tennis_dict={"player":players_list}
    return render(request,"tennis_app/winstats.html",context=tennis_dict)
def gamestats(request):
    players_list=tennis_db.objects.order_by("name")
    tennis_dict={"player":players_list}
    return render(request,"tennis_app/gamestats.html",context=tennis_dict)

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
         obj,created=tennis_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"tennis_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"tennis_app/form_player.html",{"form":form})





