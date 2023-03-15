from django.shortcuts import render
from kickboxing_app.models import kickboxing_db
from kickboxing_app.forms import playerform
from kickboxing_app.forms import aboutform
from kickboxing_app.forms import pointstatsform
from kickboxing_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"kickboxing_app/home.html")
def player(request):
    players_list=kickboxing_db.objects.order_by("name")
    kickboxing_dict={"player":players_list}
    return render(request,"kickboxing_app/player.html",context=kickboxing_dict)	
def about(request):
    players_list=kickboxing_db.objects.order_by("name")
    kickboxing_dict={"player":players_list}
    return render(request,"kickboxing_app/about.html",context=kickboxing_dict)	
def pointstats(request):
    players_list=kickboxing_db.objects.order_by("name")
    kickboxing_dict={"player":players_list}
    return render(request,"kickboxing_app/pointstats.html",context=kickboxing_dict)	
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         country=form.cleaned_data["country"]
         defaults={"age":age,"country":country}
         obj,created=kickboxing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"kickboxing_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"kickboxing_app/form_player.html",{"form":form})       		    		    		
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         height=form.cleaned_data["height"]
         weight=form.cleaned_data["weight"]
         defaults={"height":height,"weight":weight}
         obj,created=kickboxing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"kickboxing_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"kickboxing_app/form_about.html",{"form":form})  
def form_pointstats(request):
    form=pointstatsform()
    if request.method=="POST":
      form=pointstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         wins=form.cleaned_data["wins"]
         losses=form.cleaned_data["losses"]
         defaults={"wins":wins,"losses":losses}
         obj,created=kickboxing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"kickboxing_app/submit_pointstats.html")
      else:
         print("error form invalid")      
    return render(request,"kickboxing_app/form_pointstats.html",{"form":form})                                      
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=kickboxing_db.objects.get(name__iexact=name) 
         except karate_db.DoesNotExist:
             return render(request,"kickboxing_app/error_player.html")
         return render(request,"kickboxing_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"kickboxing_app/search_player.html",{"form":form})



