from django.shortcuts import render
from darts_app.models import darts_db
from darts_app.forms import playerform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"darts_app/home.html")
def player(request):
    players_list=darts_db.objects.order_by("name")
    darts_dict={"player":players_list}
    return render(request,"darts_app/player.html",context=darts_dict)
def about(request):
    players_list=darts_db.objects.order_by("name")
    darts_dict={"player":players_list}
    return render(request,"darts_app/about.html",context=darts_dict)
def details(request):
    players_list=darts_db.objects.order_by("name")
    darts_dict={"player":players_list}
    return render(request,"darts_app/details.html",context=darts_dict)	    	    
def gamestats(request):
    players_list=darts_db.objects.order_by("name")
    darts_dict={"player":players_list}
    return render(request,"darts_app/gamestats.html",context=darts_dict)
def pointstats(request):
    players_list=darts_db.objects.order_by("name")
    darts_dict={"player":players_list}
    return render(request,"darts_app/pointstats.html",context=darts_dict)
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
         obj,created=darts_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"darts_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"darts_app/form_player.html",{"form":form})
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         gender=form.cleaned_data["gender"]
         defaults={"gender":gender}
         obj,created=darts_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"darts_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"darts_app/form_about.html",{"form":form})
def form_details(request):
    form=detailsform()
    if request.method=="POST":
      form=detailsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         rank=form.cleaned_data["rank"]
         height=form.cleaned_data["height"]
         defaults={"rank":rank,"height":height}
         obj,created=darts_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"darts_app/submit_details.html")
      else:
         print("error form invalid")      
    return render(request,"darts_app/form_details.html",{"form":form})  
def form_gamestats(request):
    form=gamestatsform()
    if request.method=="POST":
      form=gamestatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         darts=form.cleaned_data["darts"]
         defaults={"darts":darts}
         obj,created=darts_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"darts_app/submit_gamestats.html")
      else:
         print("error form invalid")      
    return render(request,"darts_app/form_gamestats.html",{"form":form})
def form_pointstats(request):
    form=pointstatsform()
    if request.method=="POST":
      form=pointstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         titles=form.cleaned_data["titles"]
         finishes=form.cleaned_data["finishes"]
         defaults={"titles":titles,"finishes":finishes}
         obj,created=darts_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"darts_app/submit_pointstats.html")
      else:
         print("error form invalid")      
    return render(request,"darts_app/form_pointstats.html",{"form":form})              

