from django.shortcuts import render
from badminton_app.models import badminton_db
from badminton_app.forms import playerform
from badminton_app.forms import aboutform
from badminton_app.forms import detailsform
from badminton_app.forms import careerstatsform
from badminton_app.forms import singlesstatsform
from badminton_app.forms import doublesstatsform
from badminton_app.forms import mixedstatsform
from badminton_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"badminton_app/home.html")
def player(request):
    players_list=badminton_db.objects.order_by("name")
    badminton_dict={"player":players_list}
    return render(request,"badminton_app/player.html",context=badminton_dict)		
def about(request):
    players_list=badminton_db.objects.order_by("name")
    badminton_dict={"player":players_list}
    return render(request,"badminton_app/about.html",context=badminton_dict)
def details(request):
    players_list=badminton_db.objects.order_by("name")
    badminton_dict={"player":players_list}
    return render(request,"badminton_app/details.html",context=badminton_dict)
def careerstats(request):
    players_list=badminton_db.objects.order_by("name")
    badminton_dict={"player":players_list}
    return render(request,"badminton_app/careerstats.html",context=badminton_dict)
def singlesstats(request):
    players_list=badminton_db.objects.order_by("name")
    badminton_dict={"player":players_list}
    return render(request,"badminton_app/singlesstats.html",context=badminton_dict) 
def doublesstats(request):
    players_list=badminton_db.objects.order_by("name")
    badminton_dict={"player":players_list}
    return render(request,"badminton_app/doublesstats.html",context=badminton_dict)
def mixedstats(request):
    players_list=badminton_db.objects.order_by("name")
    badminton_dict={"player":players_list}
    return render(request,"badminton_app/mixedstats.html",context=badminton_dict)               

def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         dob=form.cleaned_data["dob"]
         country=form.cleaned_data["country"]
         defaults={"age":age,"dob":dob,"country":country}
         obj,created=badminton_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"badminton_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"badminton_app/form_player.html",{"form":form})     
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         gender=form.cleaned_data["gender"]
         rank=form.cleaned_data["rank"]
         tourrank=form.cleaned_data["tourrank"]
         defaults={"gender":gender,"rank":rank,"tourrank":tourrank}
         obj,created=badminton_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"badminton_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"badminton_app/form_about.html",{"form":form})     
def form_details(request):
    form=detailsform()
    if request.method=="POST":
      form=detailsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         debut=form.cleaned_data["debut"]
         height=form.cleaned_data["height"]
         weight=form.cleaned_data["weight"]
         defaults={"debut":debut,"height":height,"weight":weight}
         obj,created=badminton_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"badminton_app/submit_details.html")
      else:
         print("error form invalid")      
    return render(request,"badminton_app/form_details.html",{"form":form}) 
def form_careerstats(request):
    form=careerstatsform()
    if request.method=="POST":
      form=careerstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         plays=form.cleaned_data["plays"]
         careerwins=form.cleaned_data["careerwins"]
         defaults={"plays":plays,"careerwins":careerwins}
         obj,created=badminton_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"badminton_app/submit_careerstats.html")
      else:
         print("error form invalid")      
    return render(request,"badminton_app/form_careerstats.html",{"form":form})
def form_singlesstats(request):
    form=singlesstatsform()
    if request.method=="POST":
      form=singlesstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         singlesplayed=form.cleaned_data["singlesplayed"]
         singleswon=form.cleaned_data["singleswon"]
         singleslost=form.cleaned_data["singleslost"]
         defaults={"singlesplayed":singlesplayed,"singleswon":singleswon,"singleslost":singleslost}
         obj,created=badminton_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"badminton_app/submit_singlesstats.html")
      else:
         print("error form invalid")      
    return render(request,"badminton_app/form_singlesstats.html",{"form":form}) 
def form_doublesstats(request):
    form=doublesstatsform()
    if request.method=="POST":
      form=doublesstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         doublesplayed=form.cleaned_data["doublesplayed"]
         doubleswon=form.cleaned_data["doubleswon"]
         doubleslost=form.cleaned_data["doubleslost"]
         defaults={"doublesplayed":doublesplayed,"doubleswon":doubleswon,"doubleslost":doubleslost}
         obj,created=badminton_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"badminton_app/submit_doublesstats.html")
      else:
         print("error form invalid")      
    return render(request,"badminton_app/form_doublesstats.html",{"form":form}) 
def form_mixedstats(request):
    form=mixedstatsform()
    if request.method=="POST":
      form=mixedstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         mixedplayed=form.cleaned_data["mixedplayed"]
         mixedwon=form.cleaned_data["mixedwon"]
         mixedlost=form.cleaned_data["mixedlost"]
         defaults={"mixedplayed":mixedplayed,"mixedwon":mixedwon,"mixedlost":mixedlost}
         obj,created=badminton_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"badminton_app/submit_mixedstats.html")
      else:
         print("error form invalid")      
    return render(request,"badminton_app/form_mixedstats.html",{"form":form})  
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=badminton_db.objects.get(name__iexact=name) 
         except badminton_db.DoesNotExist:
             return render(request,"badminton_app/error_player.html")
         return render(request,"badminton_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"badminton_app/search_player.html",{"form":form})

