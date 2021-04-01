from django.shortcuts import render
from basketball_app.models import basketball_db
from basketball_app.forms import playerform

# Create your views here.
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"basketball_app/home.html")
def player(request):
    players_list=basketball_db.objects.order_by("name")
    basketball_dict={"player":players_list}
    return render(request,"basketball_app/player.html",context=basketball_dict)		
def about(request):
    players_list=basketball_db.objects.order_by("name")
    basketball_dict={"player":players_list}
    return render(request,"basketball_app/about.html",context=basketball_dict)
def details(request):
    players_list=basketball_db.objects.order_by("name")
    basketball_dict={"player":players_list}
    return render(request,"basketball_app/details.html",context=basketball_dict)
def gamestats(request):
    players_list=basketball_db.objects.order_by("name")
    basketball_dict={"player":players_list}
    return render(request,"basketball_app/gamestats.html",context=basketball_dict)
def goalstats(request):
    players_list=basketball_db.objects.order_by("name")
    basketball_dict={"player":players_list}
    return render(request,"basketball_app/goalstats.html",context=basketball_dict)
def pointstats(request):
    players_list=basketball_db.objects.order_by("name")
    basketball_dict={"player":players_list}
    return render(request,"basketball_app/pointstats.html",context=basketball_dict)
def blockstats(request):
    players_list=basketball_db.objects.order_by("name")
    basketball_dict={"player":players_list}
    return render(request,"basketball_app/blockstats.html",context=basketball_dict)


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
         obj,created=basketball_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"basketball_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"basketball_app/form_player.html",{"form":form})     		

def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         college=form.cleaned_data["college"]
         position=form.cleaned_data["position"]
         defaults={"college":college,"position":position}
         obj,created=basketball_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"basketball_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"basketball_app/form_about.html",{"form":form})  

def form_details(request):
    form=detailsform()
    if request.method=="POST":
      form=detailsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         height=form.cleaned_data["height"]
         weight=form.cleaned_data["weight"]
         preferedhand=form.cleaned_data["preferedhand"]
         defaults={"height":height,"weight":weight,"preferedhand":preferedhand}
         obj,created=basketball_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"basketball_app/submit_details.html")
      else:
         print("error form invalid")      
    return render(request,"basketball_app/form_details.html",{"form":form})

def form_gamestats(request):
    form=gamestatsform()
    if request.method=="POST":
      form=gamestatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         games=form.cleaned_data["games"]
         gamestarted=form.cleaned_data["gamestarted"]
         minutes=form.cleaned_data["minutes"]
         defaults={"games":games,"gamestarted":gamestarted,"minutes":minutes}
         obj,created=basketball_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"basketball_app/submit_gamestats.html")
      else:
         print("error form invalid")      
    return render(request,"basketball_app/form_gamestats.html",{"form":form})

def form_goalstats(request):
    form=goalstatsform()
    if request.method=="POST":
      form=goalstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         goals=form.cleaned_data["goals"]
         attempts=form.cleaned_data["attempts"]
         assists=form.cleaned_data["assists"]
         steals=form.cleaned_data["steals"]
         defaults={"goals":goals,"attempts":attempts,"assists":assists,"steals":steals}
         obj,created=basketball_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"basketball_app/submit_goalstats.html")
      else:
         print("error form invalid")      
    return render(request,"basketball_app/form_goalstats.html",{"form":form})


def form_pointstats(request):
    form=pointstatsform()
    if request.method=="POST":
      form=pointstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         points=form.cleaned_data["points"]
         threepoints=form.cleaned_data["threepoints"]
         twopoints=form.cleaned_data["twopoints"]
         defaults={"points":points,"threepoints":threepoints,"twopoints":twopoints}
         obj,created=basketball_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"basketball_app/submit_pointstats.html")
      else:
         print("error form invalid")      
    return render(request,"basketball_app/form_pointstats.html",{"form":form})

def form_blockstats(request):
    form=blockstatsform()
    if request.method=="POST":
      form=blockstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         blocks=form.cleaned_data["blocks"]
         freethrows=form.cleaned_data["freethrows"]
         rebounds=form.cleaned_data["rebounds"]
         fouls=form.cleaned_data["fouls"]
         defaults={"blocks":blocks,"freethrows":freethrows,"rebounds":rebounds,"fouls":fouls}
         obj,created=basketball_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"basketball_app/submit_blockstats.html")
      else:
         print("error form invalid")      
    return render(request,"basketball_app/form_blockstats.html",{"form":form})















