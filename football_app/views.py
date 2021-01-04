from django.shortcuts import render
from football_app.models import football_db
from football_app.forms import playerform


def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"football_app/home.html")
def player(request):
    players_list=football_db.objects.order_by("name")
    football_dict={"player":players_list}
    return render(request,"football_app/player.html",context=football_dict)		
def about(request):
    players_list=football_db.objects.order_by("name")
    football_dict={"player":players_list}
    return render(request,"football_app/about.html",context=football_dict)
def details(request):
    players_list=football_db.objects.order_by("name")
    football_dict={"player":players_list}
    return render(request,"football_app/details.html",context=football_dict)
def matchstats(request):
    players_list=football_db.objects.order_by("name")
    football_dict={"player":players_list}
    return render(request,"football_app/matchstats.html",context=football_dict)
def goalstats(request):
    players_list=football_db.objects.order_by("name")
    football_dict={"player":players_list}
    return render(request,"football_app/goalstats.html",context=football_dict)
def penaltystats(request):
    players_list=football_db.objects.order_by("name")
    football_dict={"player":players_list}
    return render(request,"football_app/penaltystats.html",context=football_dict)
def cardstats(request):
    players_list=football_db.objects.order_by("name")
    football_dict={"player":players_list}
    return render(request,"football_app/cardstats.html",context=football_dict)

def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         dob=form.cleaned_data["dob"]
         nationality=form.cleaned_data["nationality"]
         birthplace=form.cleaned_data["birthplace"]
         defaults={"age":age,"dob":dob,"nationality":nationality,"birthplace":birthplace}
         obj,created=football_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"football_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"football_app/form_player.html",{"form":form})

def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         fifaid=form.cleaned_data["fifaid"]
         debut=form.cleaned_data["debut"]
         position=form.cleaned_data["position"]
         defaults={"fifaid":fifaid,"debut":debut,"position":position}
         obj,created=football_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"football_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"football_app/form_about.html",{"form":form}) 

def form_details(request):
    form=detailsform()
    if request.method=="POST":
      form=detailsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         league=form.cleaned_data["league"]
         club=form.cleaned_data["club"]
         height=form.cleaned_data["height"]
         weight=form.cleaned_data["weight"]
         foot=form.cleaned_data["foot"]
         defaults={"league":league,"club":club,"height":height,"weight":weight,"foot":foot}
         obj,created=football_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"football_app/submit_details.html")
      else:
         print("error form invalid")      
    return render(request,"football_app/form_details.html",{"form":form}) 

def form_matchstats(request):
    form=matchstatsform()
    if request.method=="POST":
      form=matchstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         matches=form.cleaned_data["matches"]
         defaults={"matches":matches}
         obj,created=football_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"football_app/submit_matchstats.html")
      else:
         print("error form invalid")      
    return render(request,"football_app/form_matchstats.html",{"form":form}) 

def form_goalstats(request):
    form=goalstatsrform()
    if request.method=="POST":
      form=goalstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         goals=form.cleaned_data["goals"]
         assists=form.cleaned_data["assists"]
         goalsconceded=form.cleaned_data["goalsconceded"]
         defaults={"goals":goals,"assists":assists,"goalsconceded":goalsconceded}
         obj,created=football_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"football_app/submit_goalstats.html")
      else:
         print("error form invalid")      
    return render(request,"football_app/form_goalstats.html",{"form":form})

def form_penaltystats(request):
    form=penaltystatsform()
    if request.method=="POST":
      form=penaltystatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         penaltyscored=form.cleaned_data["penaltyscored"]
         penaltymissed=form.cleaned_data["penaltymissed"]
         defaults={"penaltyscored":penaltyscored,"penaltymissed":penaltymissed}
         obj,created=football_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"football_app/submit_penaltystats.html")
      else:
         print("error form invalid")      
    return render(request,"football_app/form_penaltystats.html",{"form":form}) 


def form_cardstats(request):
    form=cardstatsform()
    if request.method=="POST":
      form=cardstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         yellowcards=form.cleaned_data["yellowcards"]
         redcards=form.cleaned_data["redcards"]
         defaults={"yellowcards":yellowcards,"redcards":redcards}
         obj,created=football_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"football_app/submit_cardstats.html")
      else:
         print("error form invalid")      
    return render(request,"football_app/form_cardstats.html",{"form":form}) 








    		







