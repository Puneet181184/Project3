from django.shortcuts import render
from golf_app.models import golf_db
from golf_app.forms import playerform
from golf_app.forms import aboutform
from golf_app.forms import detailsform
from golf_app.forms import gamestatsform
from golf_app.forms import positionstatsform
from golf_app.forms import pointstatsform
from golf_app.forms import searchform

# Create your views here.
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"golf_app/home.html")
def player(request):
    players_list=golf_db.objects.order_by("name")
    golf_dict={"player":players_list}
    return render(request,"golf_app/player.html",context=golf_dict)			
def about(request):
    players_list=golf_db.objects.order_by("name")
    golf_dict={"player":players_list}
    return render(request,"golf_app/about.html",context=golf_dict)     
def details(request):
    players_list=golf_db.objects.order_by("name")
    golf_dict={"player":players_list}
    return render(request,"golf_app/details.html",context=golf_dict)
def gamestats(request):
    players_list=golf_db.objects.order_by("name")
    golf_dict={"player":players_list}
    return render(request,"golf_app/gamestats.html",context=golf_dict) 
def positionstats(request):
    players_list=golf_db.objects.order_by("name")
    golf_dict={"player":players_list}
    return render(request,"golf_app/positionstats.html",context=golf_dict) 
def pointstats(request):
    players_list=golf_db.objects.order_by("name")
    golf_dict={"player":players_list}
    return render(request,"golf_app/pointstats.html",context=golf_dict)  

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
         obj,created=golf_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"golf_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"golf_app/form_player.html",{"form":form}) 
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         currentrank=form.cleaned_data["currentrank"]
         bestrank=form.cleaned_data["bestrank"]
         defaults={"currentrank":currentrank,"bestrank":bestrank}
         obj,created=golf_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"golf_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"golf_app/form_about.html",{"form":form})
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
         obj,created=golf_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"golf_app/submit_details.html")
      else:
         print("error form invalid")      
    return render(request,"golf_app/form_details.html",{"form":form})          
def form_gamestats(request):
    form=gamestatsform()
    if request.method=="POST":
      form=gamestatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         events=form.cleaned_data["events"]
         madecuts=form.cleaned_data["madecuts"]
         defaults={"events":events,"madecuts":madecuts}
         obj,created=golf_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"golf_app/submit_gamestats.html")
      else:
         print("error form invalid")      
    return render(request,"golf_app/form_gamestats.html",{"form":form})
def form_positionstats(request):
    form=positionstatsform()
    if request.method=="POST":
      form=positionstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         first=form.cleaned_data["first"]
         second=form.cleaned_data["second"]
         third=form.cleaned_data["third"]
         fourth=form.cleaned_data["fourth"]
         defaults={"first":first,"second":second,"third":third,"fourth":fourth}
         obj,created=golf_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"golf_app/submit_positionstats.html")
      else:
         print("error form invalid")      
    return render(request,"golf_app/form_positionstats.html",{"form":form}) 
def form_pointstats(request):
    form=pointstatsform()
    if request.method=="POST":
      form=pointstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         totalpoints=form.cleaned_data["totalpoints"]
         averagepoints=form.cleaned_data["averagepoints"]
         divisor=form.cleaned_data["divisor"]
         defaults={"totalpoints":totalpoints,"averagepoints":averagepoints,"divisor":divisor}
         obj,created=golf_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"golf_app/submit_pointstats.html")
      else:
         print("error form invalid")      
    return render(request,"golf_app/form_pointstats.html",{"form":form})             
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=golf_db.objects.get(name__iexact=name) 
         except golf_db.DoesNotExist:
             return render(request,"golf_app/error_player.html")
         return render(request,"golf_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"golf_app/search_player.html",{"form":form})  
def search_about(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=golf_db.objects.get(name__iexact=name) 
         except golf_db.DoesNotExist:
             return render(request,"golf_app/error_about.html")
         return render(request,"golf_app/result_about.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"golf_app/search_about.html",{"form":form}) 
def search_details(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=golf_db.objects.get(name__iexact=name) 
         except golf_db.DoesNotExist:
             return render(request,"golf_app/error_details.html")
         return render(request,"golf_app/result_details.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"golf_app/search_details.html",{"form":form})
def search_gamestats(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=golf_db.objects.get(name__iexact=name) 
         except golf_db.DoesNotExist:
             return render(request,"golf_app/error_gamestats.html")
         return render(request,"golf_app/result_gamestats.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"golf_app/search_gamestats.html",{"form":form}) 
def search_positionstats(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=golf_db.objects.get(name__iexact=name) 
         except golf_db.DoesNotExist:
             return render(request,"golf_app/error_positionstats.html")
         return render(request,"golf_app/result_positionstats.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"golf_app/search_positionstats.html",{"form":form})
def search_pointstats(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=golf_db.objects.get(name__iexact=name) 
         except golf_db.DoesNotExist:
             return render(request,"golf_app/error_pointstats.html")
         return render(request,"golf_app/result_pointstats.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"golf_app/search_pointstats.html",{"form":form})  














