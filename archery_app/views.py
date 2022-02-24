from django.shortcuts import render
from archery_app.models import archery_db
from archery_app.forms import playerform
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"archery_app/home.html")
def player(request):
    players_list=archery_db.objects.order_by("name")
    archery_dict={"player":players_list}
    return render(request,"archery_app/player.html",context=archery_dict)		
def about(request):
    players_list=archery_db.objects.order_by("name")
    archery_dict={"player":players_list}
    return render(request,"archery_app/about.html",context=archery_dict)		    
def details(request):
    players_list=archery_db.objects.order_by("name")
    archery_dict={"player":players_list}
    return render(request,"archery_app/details.html",context=archery_dict)		    
def gamestats(request):
    players_list=archery_db.objects.order_by("name")
    archery_dict={"player":players_list}
    return render(request,"archery_app/gamestats.html",context=archery_dict)	
def pointstats(request):
    players_list=archery_db.objects.order_by("name")
    archery_dict={"player":players_list}
    return render(request,"archery_app/pointstats.html",context=archery_dict)
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
         obj,created=archery_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"archery_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"archery_app/form_player.html",{"form":form})     
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         debut=form.cleaned_data["debut"]
         gender=form.cleaned_data["gender"]
         defaults={"debut":debut,"gender":gender}
         obj,created=archery_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"archery_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"archery_app/form_about.html",{"form":form}) 
def form_details(request):
    form=detailsform()
    if request.method=="POST":
      form=detailsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         rank=form.cleaned_data["rank"]
         defaults={"rank":rank}
         obj,created=archery_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"archery_app/submit_details.html")
      else:
         print("error form invalid")      
    return render(request,"archery_app/form_details.html",{"form":form})   
def form_gamestats(request):
    form=gamestatsform()
    if request.method=="POST":
      form=gamestatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         arrowlength=form.cleaned_data["arrowlength"]
         drawweight=form.cleaned_data["drawweight"]
         averagearrow=form.cleaned_data["averagearrow"]
         defaults={"arrowlength":arrowlength,"drawweight":drawweight,"averagearrow":averagearrow}
         obj,created=archery_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"archery_app/submit_gamestats.html")
      else:
         print("error form invalid")      
    return render(request,"archery_app/form_gamestats.html",{"form":form})     
def form_pointstats(request):
    form=pointstatsform()
    if request.method=="POST":
      form=pointstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         worldcupgold=form.cleaned_data["worldcupgold"]
         worldcupsilver=form.cleaned_data["worldcupsilver"]
         worldcupbronze=form.cleaned_data["worldcupbronze"]
         defaults={"worldcupgold":worldcupgold,"worldcupsilver":worldcupsilver,"worldcupbronze":worldcupbronze}
         obj,created=archery_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"archery_app/submit_pointstats.html")
      else:
         print("error form invalid")      
    return render(request,"archery_app/form_pointstats.html",{"form":form})     



                                                