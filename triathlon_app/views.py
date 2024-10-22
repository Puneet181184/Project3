from django.shortcuts import render
from triathlon_app.models import triathlon_db
from triathlon_app.forms import playerform
from triathlon_app.forms import aboutform
from triathlon_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"triathlon_app/home.html")
def player(request):
    players_list=triathlon_db.objects.order_by("name")
    triathlon_dict={"player":players_list}
    return render(request,"triathlon_app/player.html",context=triathlon_dict)		
def about(request):
    players_list=triathlon_db.objects.order_by("name")
    triathlon_dict={"player":players_list}
    return render(request,"triathlon_app/about.html",context=triathlon_dict)	
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         dob=form.cleaned_data["dob"]
         country=form.cleaned_data["country"]
         defaults={"dob":dob,"country":country}
         obj,created=triathlon_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"triathlon_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"triathlon_app/form_player.html",{"form":form})

def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         gender=form.cleaned_data["gender"]
         rank=form.cleaned_data["rank"]
         wins=form.cleaned_data["wins"]
         defaults={"gender":gender,"rank":rank,"wins":wins}
         obj,created=triathlon_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"triathlon_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"triathlon_app/form_about.html",{"form":form})
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=triathlon_db.objects.get(name__iexact=name) 
         except tennis_db.DoesNotExist:
             return render(request,"triathlon_app/error_player.html")
         return render(request,"triathlon_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"triathlon_app/search_player.html",{"form":form})

def search_about(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=triathlon_db.objects.get(name__iexact=name) 
         except tennis_db.DoesNotExist:
             return render(request,"triathlon_app/error_about.html")
         return render(request,"triathlon_app/result_about.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"triathlon_app/search_about.html",{"form":form})  
