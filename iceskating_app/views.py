from django.shortcuts import render
from iceskating_app.models import iceskating_db
from iceskating_app.forms import playerform
from iceskating_app.forms import aboutform
from iceskating_app.forms import detailsform
from iceskating_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"iceskating_app/home.html")
def player(request):
    players_list=iceskating_db.objects.order_by("name")
    iceskating_dict={"player":players_list}
    return render(request,"iceskating_app/player.html",context=iceskating_dict)			
def about(request):
    players_list=iceskating_db.objects.order_by("name")
    iceskating_dict={"player":players_list}
    return render(request,"iceskating_app/about.html",context=iceskating_dict)			
def details(request):
    players_list=iceskating_db.objects.order_by("name")
    iceskating_dict={"player":players_list}
    return render(request,"iceskating_app/details.html",context=iceskating_dict)			
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         country=form.cleaned_data["country"]
         defaults={"age":age,"country":country}
         obj,created=iceskating_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"iceskating_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"iceskating_app/form_player.html",{"form":form})       
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         height=form.cleaned_data["height"]
         weight=form.cleaned_data["weight"]
         defaults={"height":height,"weight":weight}
         obj,created=iceskating_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"iceskating_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"iceskating_app/form_about.html",{"form":form}) 
def form_details(request):
    form=detailsform()
    if request.method=="POST":
      form=detailsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         level=form.cleaned_data["level"]
         defaults={"level":level}
         obj,created=iceskating_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"iceskating_app/submit_details.html")
      else:
         print("error form invalid")      
    return render(request,"iceskating_app/form_details.html",{"form":form})
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=iceskating_db.objects.get(name__iexact=name) 
         except iceskating_db.DoesNotExist:
             return render(request,"iceskating_app/error_player.html")
         return render(request,"iceskating_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"iceskating_app/search_player.html",{"form":form}) 
def search_about(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=iceskating_db.objects.get(name__iexact=name) 
         except iceskating_db.DoesNotExist:
             return render(request,"iceskating_app/error_about.html")
         return render(request,"iceskating_app/result_about.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"iceskating_app/search_about.html",{"form":form}) 
def search_details(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=iceskating_db.objects.get(name__iexact=name) 
         except iceskating_db.DoesNotExist:
             return render(request,"iceskating_app/error_details.html")
         return render(request,"iceskating_app/result_details.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"iceskating_app/search_details.html",{"form":form})               
