from django.shortcuts import render
from karate_app.models import karate_db
from karate_app.forms import playerform
from karate_app.forms import aboutform
from karate_app.forms import detailsform
from karate_app.forms import pointstatsform
from karate_app.forms import searchform
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"karate_app/home.html")
def player(request):
    players_list=karate_db.objects.order_by("name")
    karate_dict={"player":players_list}
    return render(request,"karate_app/player.html",context=karate_dict)		
def about(request):
    players_list=karate_db.objects.order_by("name")
    karate_dict={"player":players_list}
    return render(request,"karate_app/about.html",context=karate_dict)	
def details(request):
    players_list=karate_db.objects.order_by("name")
    karate_dict={"player":players_list}
    return render(request,"karate_app/details.html",context=karate_dict)
def pointstats(request):
    players_list=karate_db.objects.order_by("name")
    karate_dict={"player":players_list}
    return render(request,"karate_app/pointstats.html",context=karate_dict)	
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         country=form.cleaned_data["country"]
         defaults={"age":age,"country":country}
         obj,created=karate_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"karate_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"karate_app/form_player.html",{"form":form})   
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         gender=form.cleaned_data["gender"]
         defaults={"gender":gender}
         obj,created=karate_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"karate_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"karate_app/form_about.html",{"form":form}) 
def form_details(request):
    form=detailsform()
    if request.method=="POST":
      form=detailsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         rank=form.cleaned_data["rank"]
         category=form.cleaned_data["category"]
         defaults={"rank":rank,"category":category}
         obj,created=karate_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"karate_app/submit_details.html")
      else:
         print("error form invalid")      
    return render(request,"karate_app/form_details.html",{"form":form})  
def form_pointstats(request):
    form=pointstatsform()
    if request.method=="POST":
      form=pointstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         worldgold=form.cleaned_data["worldgold"]
         worldsilver=form.cleaned_data["worldsilver"]
         worldbronze=form.cleaned_data["worldbronze"]
         defaults={"worldgold":worldgold,"worldsilver":worldsilver,"worldbronze":worldbronze}
         obj,created=karate_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"karate_app/submit_pointstats.html")
      else:
         print("error form invalid")      
    return render(request,"karate_app/form_pointstats.html",{"form":form})      
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=karate_db.objects.get(name__iexact=name) 
         except karate_db.DoesNotExist:
             return render(request,"karate_app/error_player.html")
         return render(request,"karate_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"karate_app/search_player.html",{"form":form})
def search_about(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=karate_db.objects.get(name__iexact=name) 
         except karate_db.DoesNotExist:
             return render(request,"karate_app/error_about.html")
         return render(request,"karate_app/result_about.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"karate_app/search_about.html",{"form":form}) 
def search_details(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=karate_db.objects.get(name__iexact=name) 
         except karate_db.DoesNotExist:
             return render(request,"karate_app/error_details.html")
         return render(request,"karate_app/result_details.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"karate_app/search_details.html",{"form":form}) 
def search_pointstats(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=karate_db.objects.get(name__iexact=name) 
         except karate_db.DoesNotExist:
             return render(request,"karate_app/error_pointstats.html")
         return render(request,"karate_app/result_pointstats.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"karate_app/search_pointstats.html",{"form":form})          