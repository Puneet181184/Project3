from django.shortcuts import render
from tabletennis_app.models import tabletennis_db
from tabletennis_app.forms import playerform
from tabletennis_app.forms import aboutform
from tabletennis_app.forms import detailsform
from tabletennis_app.forms import careerstatsform
from tabletennis_app.forms import singlesstatsform
from tabletennis_app.forms import doublesstatsform
from tabletennis_app.forms import totalstatsform
from tabletennis_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"tabletennis_app/home.html")
def player(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/player.html",context=tabletennis_dict)			
def about(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/about.html",context=tabletennis_dict) 
def details(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/details.html",context=tabletennis_dict)
def careerstats(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/careerstats.html",context=tabletennis_dict) 
def singlesstats(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/singlesstats.html",context=tabletennis_dict)
def doublesstats(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/doublesstats.html",context=tabletennis_dict)
def totalstats(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/totalstats.html",context=tabletennis_dict)                                                      

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
         obj,created=tabletennis_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"tabletennis_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"tabletennis_app/form_player.html",{"form":form})   
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         gender=form.cleaned_data["gender"]
         rank=form.cleaned_data["rank"]
         bestrank=form.cleaned_data["bestrank"]
         defaults={"gender":gender,"rank":rank,"bestrank":bestrank}
         obj,created=tabletennis_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"tabletennis_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"tabletennis_app/form_about.html",{"form":form})
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
         obj,created=tabletennis_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"tabletennis_app/submit_details.html")
      else:
         print("error form invalid")      
    return render(request,"tabletennis_app/form_details.html",{"form":form}) 
def form_careerstats(request):
    form=careerstatsform()
    if request.method=="POST":
      form=careerstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         plays=form.cleaned_data["plays"]
         grip=form.cleaned_data["grip"]
         defaults={"plays":plays,"grip":grip}
         obj,created=tabletennis_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"tabletennis_app/submit_careerstats.html")
      else:
         print("error form invalid")      
    return render(request,"tabletennis_app/form_careerstats.html",{"form":form})       
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
         obj,created=tabletennis_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"tabletennis_app/submit_singlesstats.html")
      else:
         print("error form invalid")      
    return render(request,"tabletennis_app/form_singlesstats.html",{"form":form})
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
         obj,created=tabletennis_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"tabletennis_app/submit_doublesstats.html")
      else:
         print("error form invalid")      
    return render(request,"tabletennis_app/form_doublesstats.html",{"form":form}) 
def form_totalstats(request):
    form=totalstatsform()
    if request.method=="POST":
      form=totalstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         totalplayed=form.cleaned_data["totalplayed"]
         totalwon=form.cleaned_data["totalwon"]
         totallost=form.cleaned_data["totallost"]
         defaults={"totalplayed":totalplayed,"totalwon":totalwon,"totallost":totallost}
         obj,created=tabletennis_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"tabletennis_app/submit_totalstats.html")
      else:
         print("error form invalid")      
    return render(request,"tabletennis_app/form_totalstats.html",{"form":form})       
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=tabletennis_db.objects.get(name__iexact=name) 
         except tabletennis_db.DoesNotExist:
             return render(request,"tabletennis_app/error_player.html")
         return render(request,"tabletennis_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"tabletennis_app/search_player.html",{"form":form})
