from django.shortcuts import render
from fencing_app.models import fencing_db
from fencing_app.forms import playerform
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"fencing_app/home.html")
def player(request):
    players_list=fencing_db.objects.order_by("name")
    fencing_dict={"player":players_list}
    return render(request,"fencing_app/player.html",context=fencing_dict)		
def about(request):
    players_list=fencing_db.objects.order_by("name")
    fencing_dict={"player":players_list}
    return render(request,"fencing_app/about.html",context=fencing_dict)
def details(request):
    players_list=fencing_db.objects.order_by("name")
    fencing_dict={"player":players_list}
    return render(request,"fencing_app/details.html",context=fencing_dict)	
def gamestats(request):
    players_list=fencing_db.objects.order_by("name")
    fencing_dict={"player":players_list}
    return render(request,"fencing_app/gamestats.html",context=fencing_dict)
def pointstats(request):
    players_list=fencing_db.objects.order_by("name")
    fencing_dict={"player":players_list}
    return render(request,"fencing_app/pointstats.html",context=fencing_dict)		    		    	    
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
         obj,created=fencing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"fencing_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"fencing_app/form_player.html",{"form":form})   
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         debut=form.cleaned_data["debut"]
         gender=form.cleaned_data["gender"]
         defaults={"debut":debut,"gender":gender}
         obj,created=fencing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"fencing_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"fencing_app/form_about.html",{"form":form})  
def form_details(request):
    form=detailsform()
    if request.method=="POST":
      form=detailsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         rank=form.cleaned_data["rank"]
         style=form.cleaned_data["style"]
         defaults={"rank":rank,"style":style}
         obj,created=fencing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"fencing_app/submit_details.html")
      else:
         print("error form invalid")      
    return render(request,"fencing_app/form_details.html",{"form":form})  
def form_gamestats(request):
    form=gamestatsform()
    if request.method=="POST":
      form=gamestatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         hand=form.cleaned_data["hand"]
         defaults={"hand":hand}
         obj,created=fencing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"fencing_app/submit_gamestats.html")
      else:
         print("error form invalid")      
    return render(request,"fencing_app/form_gamestats.html",{"form":form})  
def form_pointstats(request):
    form=pointstatsform()
    if request.method=="POST":
      form=pointstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         points=form.cleaned_data["points"]
         worldcupgold=form.cleaned_data["worldcupgold"]
         worldcupsilver=form.cleaned_data["worldcupsilver"]
         worldcupbronze=form.cleaned_data["worldcupbronze"]
         defaults={"points":points,"worldcupgold":worldcupgold,"worldcupsilver":worldcupsilver,"worldcupbronze":worldcupbronze}
         obj,created=fencing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"fencing_app/submit_pointstats.html")
      else:
         print("error form invalid")      
    return render(request,"fencing_app/form_pointstats.html",{"form":form})                      