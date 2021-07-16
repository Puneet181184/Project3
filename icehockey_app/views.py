from django.shortcuts import render
from icehockey_app.models import icehockey_db
from icehockey_app.forms import playerform
from icehockey_app.forms import aboutform
from icehockey_app.forms import detailsform
from icehockey_app.forms import gamestatsform
from icehockey_app.forms import goalstatsform
from icehockey_app.forms import pointstatsform
from icehockey_app.forms import shotstatsform
from icehockey_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"icehockey_app/home.html")
def player(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/player.html",context=icehockey_dict)		
def about(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/about.html",context=icehockey_dict)       
def details(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/details.html",context=icehockey_dict) 
def gamestats(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/gamestats.html",context=icehockey_dict)
def goalstats(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/goalstats.html",context=icehockey_dict)
def pointstats(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/pointstats.html",context=icehockey_dict)
def shotstats(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/shotstats.html",context=icehockey_dict)       
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
         obj,created=icehockey_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"icehockey_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"icehockey_app/form_player.html",{"form":form})
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         team=form.cleaned_data["team"]
         position=form.cleaned_data["position"]
         defaults={"team":team,"position":position}
         obj,created=icehockey_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"icehockey_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"icehockey_app/form_about.html",{"form":form})
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
         obj,created=icehockey_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"icehockey_app/submit_details.html")
      else:
         print("error form invalid")      
    return render(request,"icehockey_app/form_details.html",{"form":form})
def form_gamestats(request):
    form=gamestatsform()
    if request.method=="POST":
      form=gamestatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         games=form.cleaned_data["games"]
         assists=form.cleaned_data["assists"]
         defaults={"games":games,"assists":assists,}
         obj,created=icehockey_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"icehockey_app/submit_gamestats.html")
      else:
         print("error form invalid")      
    return render(request,"icehockey_app/form_gamestats.html",{"form":form})
def form_goalstats(request):
    form=goalstatsform()
    if request.method=="POST":
      form=goalstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         goals=form.cleaned_data["goals"]
         powerplaygoals=form.cleaned_data["powerplaygoals"]
         shorthandgoals=form.cleaned_data["shorthandgoals"]
         wininggoals=form.cleaned_data["wininggoals"]
         overtimegoals=form.cleaned_data["overtimegoals"]
         defaults={"goals":goals,"powerplaygoals":powerplaygoals,"shorthandgoals":shorthandgoals,"wininggoals":wininggoals
         ,"overtimegoals":overtimegoals}
         obj,created=icehockey_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"icehockey_app/submit_goalstats.html")
      else:
         print("error form invalid")      
    return render(request,"icehockey_app/form_goalstats.html",{"form":form})
def form_pointstats(request):
    form=pointstatsform()
    if request.method=="POST":
      form=pointstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         points=form.cleaned_data["points"]
         powerplaypoints=form.cleaned_data["powerplaypoints"]
         shorthandpoints=form.cleaned_data["shorthandpoints"]
         defaults={"points":points,"powerplaypoints":powerplaypoints,"shorthandpoints":shorthandpoints}
         obj,created=icehockey_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"icehockey_app/submit_pointstats.html")
      else:
         print("error form invalid")      
    return render(request,"icehockey_app/form_pointstats.html",{"form":form})
def form_shotstats(request):
    form=shotstatsform()
    if request.method=="POST":
      form=shotstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         shots=form.cleaned_data["shots"]
         shotspercentage=form.cleaned_data["shotspercentage"]
         penaltyminutes=form.cleaned_data["penaltyminutes"]
         winspercentage=form.cleaned_data["winspercentage"]
         defaults={"shots":shots,"shotspercentage":shotspercentage,"penaltyminutes":penaltyminutes,"winspercentage":winspercentage}
         obj,created=icehockey_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"icehockey_app/submit_shotstats.html")
      else:
         print("error form invalid")      
    return render(request,"icehockey_app/form_shotstats.html",{"form":form})

def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=icehockey_db.objects.get(name__iexact=name) 
         except icehockey_db.DoesNotExist:
             return render(request,"icehockey_app/error_player.html")
         return render(request,"icehockey_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"icehockey_app/search_player.html",{"form":form})    

def search_about(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=icehockey_db.objects.get(name__iexact=name) 
         except icehockey_db.DoesNotExist:
             return render(request,"icehockey_app/error_about.html")
         return render(request,"icehockey_app/result_about.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"icehockey_app/search_about.html",{"form":form})  
def search_details(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=icehockey_db.objects.get(name__iexact=name) 
         except icehockey_db.DoesNotExist:
             return render(request,"icehockey_app/error_details.html")
         return render(request,"icehockey_app/result_details.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"icehockey_app/search_details.html",{"form":form})    
def search_gamestats(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=icehockey_db.objects.get(name__iexact=name) 
         except icehockey_db.DoesNotExist:
             return render(request,"icehockey_app/error_gamestats.html")
         return render(request,"icehockey_app/result_gamestats.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"icehockey_app/search_gamestats.html",{"form":form})    
def search_goalstats(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=icehockey_db.objects.get(name__iexact=name) 
         except icehockey_db.DoesNotExist:
             return render(request,"icehockey_app/error_goalstats.html")
         return render(request,"icehockey_app/result_goalstats.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"icehockey_app/search_goalstats.html",{"form":form}) 
def search_pointstats(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=icehockey_db.objects.get(name__iexact=name) 
         except icehockey_db.DoesNotExist:
             return render(request,"icehockey_app/error_pointstats.html")
         return render(request,"icehockey_app/result_pointstats.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"icehockey_app/search_pointstats.html",{"form":form}) 
def search_shotstats(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=icehockey_db.objects.get(name__iexact=name) 
         except icehockey_db.DoesNotExist:
             return render(request,"icehockey_app/error_shotstats.html")
         return render(request,"icehockey_app/result_shotstats.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"icehockey_app/search_shotstats.html",{"form":form})    
























