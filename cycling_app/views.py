from django.shortcuts import render
from cycling_app.models import cycling_db
from cycling_app.forms import playerform
from cycling_app.forms import aboutform
from cycling_app.forms import detailsform
from cycling_app.forms import gamestatsform
from cycling_app.forms import pointstatsform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"cycling_app/home.html")
def player(request):
    players_list=cycling_db.objects.order_by("name")
    cycling_dict={"player":players_list}
    return render(request,"cycling_app/player.html",context=cycling_dict)		
def about(request):
    players_list=cycling_db.objects.order_by("name")
    cycling_dict={"player":players_list}
    return render(request,"cycling_app/about.html",context=cycling_dict)		    
def details(request):
    players_list=cycling_db.objects.order_by("name")
    cycling_dict={"player":players_list}
    return render(request,"cycling_app/details.html",context=cycling_dict)		    
def gamestats(request):
    players_list=cycling_db.objects.order_by("name")
    cycling_dict={"player":players_list}
    return render(request,"cycling_app/gamestats.html",context=cycling_dict)	
def pointstats(request):
    players_list=cycling_db.objects.order_by("name")
    cycling_dict={"player":players_list}
    return render(request,"cycling_app/pointstats.html",context=cycling_dict)
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
         obj,created=cycling_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"cycling_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"cycling_app/form_player.html",{"form":form})    
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         debut=form.cleaned_data["debut"]
         gender=form.cleaned_data["gender"]
         defaults={"debut":debut,"gender":gender}
         obj,created=cycling_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"cycling_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"cycling_app/form_about.html",{"form":form})  
def form_details(request):
    form=detailsform()
    if request.method=="POST":
      form=detailsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         rank=form.cleaned_data["rank"]
         height=form.cleaned_data["height"]
         weight=form.cleaned_data["weight"]
         defaults={"rank":rank,"height":height,"weight":weight}
         obj,created=cycling_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"cycling_app/submit_details.html")
      else:
         print("error form invalid")      
    return render(request,"cycling_app/form_details.html",{"form":form}) 
def form_gamestats(request):
    form=gamestatsform()
    if request.method=="POST":
      form=gamestatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         grandtours=form.cleaned_data["grandtours"]
         classics=form.cleaned_data["classics"]
         defaults={"grandtours":grandtours,"classics":classics}
         obj,created=cycling_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"cycling_app/submit_gamestats.html")
      else:
         print("error form invalid")      
    return render(request,"cycling_app/form_gamestats.html",{"form":form}) 
def form_pointstats(request):
    form=pointstatsform()
    if request.method=="POST":
      form=pointstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         points=form.cleaned_data["points"]
         wins=form.cleaned_data["wins"]
         defaults={"points":points,"wins":wins}
         obj,created=cycling_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"cycling_app/submit_pointstats.html")
      else:
         print("error form invalid")      
    return render(request,"cycling_app/form_pointstats.html",{"form":form})        
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=cycling_db.objects.get(name__iexact=name) 
         except cycling_db.DoesNotExist:
             return render(request,"cycling_app/error_player.html")
         return render(request,"cycling_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"cycling_app/search_player.html",{"form":form})
