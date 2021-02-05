from django.shortcuts import render
from tennis_app.models import tennis_db
from tennis_app.forms import playerform
from tennis_app.forms import aboutform
from tennis_app.forms import detailsform
from tennis_app.forms import careerstatsform
from tennis_app.forms import pointstatsform
from tennis_app.forms import winstatsform
from tennis_app.forms import gamestatsform
from tennis_app.forms import searchform

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

def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         rank=form.cleaned_data["rank"]
         debut=form.cleaned_data["debut"]
         defaults={"rank":rank,"debut":debut}
         obj,created=tennis_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"tennis_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"tennis_app/form_about.html",{"form":form})

def form_details(request):
    form=detailsform()
    if request.method=="POST":
      form=detailsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         seasons=form.cleaned_data["seasons"]
         height=form.cleaned_data["height"]
         weight=form.cleaned_data["weight"]
         preferedhand=form.cleaned_data["preferedhand"]
         defaults={"seasons":seasons,"height":height,"weight":weight,"preferedhand":preferedhand}
         obj,created=tennis_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"tennis_app/submit_details.html")
      else:
         print("error form invalid")      
    return render(request,"tennis_app/form_details.html",{"form":form})

def form_careerstats(request):
    form=careerstatsform()
    if request.method=="POST":
      form=careerstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         titles=form.cleaned_data["titles"]
         grandslams=form.cleaned_data["grandslams"]
         tourfinals=form.cleaned_data["tourfinals"]
         masters=form.cleaned_data["masters"]
         daviscups=form.cleaned_data["daviscups"]
         defaults={"titles":titles,"grandslams":grandslams,"tourfinals":tourfinals,"masters":masters,"daviscups":daviscups}
         obj,created=tennis_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"tennis_app/submit_careerstats.html")
      else:
         print("error form invalid")      
    return render(request,"tennis_app/form_careerstats.html",{"form":form})

def form_pointstats(request):
    form=pointstatsform()
    if request.method=="POST":
      form=pointstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         totalpoints=form.cleaned_data["totalpoints"]
         tournamentpoints=form.cleaned_data["tournamentpoints"]
         rankingpoints=form.cleaned_data["rankingpoints"]
         defaults={"totalpoints":totalpoints,"tournamentpoints":tournamentpoints,"rankingpoints":rankingpoints}
         obj,created=tennis_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"tennis_app/submit_pointstats.html")
      else:
         print("error form invalid")      
    return render(request,"tennis_app/form_pointstats.html",{"form":form})

def form_winstats(request):
    form=winstatsform()
    if request.method=="POST":
      form=winstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         overallwins=form.cleaned_data["overallwins"]
         hardwins=form.cleaned_data["hardwins"]
         claywins=form.cleaned_data["claywins"]
         grasswins=form.cleaned_data["grasswins"]
         carpetwins=form.cleaned_data["carpetwins"]
         defaults={"overallwins":overallwins,"hardwins":hardwins,"claywins":claywins,"grasswins":grasswins,"carpetwins":carpetwins}
         obj,created=tennis_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"tennis_app/submit_winstats.html")
      else:
         print("error form invalid")      
    return render(request,"tennis_app/form_winstats.html",{"form":form})

def form_gamestats(request):
    form=gamestatsform()
    if request.method=="POST":
      form=gamestatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         games=form.cleaned_data["games"]
         aces=form.cleaned_data["aces"]
         faults=form.cleaned_data["faults"]
         defaults={"games":games,"aces":aces,"faults":faults}
         obj,created=tennis_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"tennis_app/submit_gamestats.html")
      else:
         print("error form invalid")      
    return render(request,"tennis_app/form_gamestats.html",{"form":form})

def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=tennis_db.objects.get(name__iexact=name) 
         except tennis_db.DoesNotExist:
             return render(request,"tennis_app/error_player.html")
         return render(request,"tennis_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"tennis_app/search_player.html",{"form":form})

    
















