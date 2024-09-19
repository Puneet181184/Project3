from django.shortcuts import render
from hockey_app.models import hockey_db
from hockey_app.forms import playerform
from hockey_app.forms import aboutform
from hockey_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"hockey_app/home.html")
def player(request):
    players_list=hockey_db.objects.order_by("name")
    hockey_dict={"player":players_list}
    return render(request,"hockey_app/player.html",context=hockey_dict)		
def about(request):
    players_list=hockey_db.objects.order_by("name")
    hockey_dict={"player":players_list}
    return render(request,"hockey_app/about.html",context=hockey_dict)		
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         dob=form.cleaned_data["dob"]
         country=form.cleaned_data["country"]
         defaults={"dob":dob,"country":country}
         obj,created=hockey_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"hockey_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"hockey_app/form_player.html",{"form":form}) 
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         gender=form.cleaned_data["gender"]
         height=form.cleaned_data["height"]
         weight=form.cleaned_data["weight"]
         defaults={"gender":gender,"height":height,"weight":weight,"position":position}
         obj,created=hockey_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"hockey_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"hockey_app/form_about.html",{"form":form})                     
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=hockey_db.objects.get(name__iexact=name) 
         except hocckey_db.DoesNotExist:
             return render(request,"hockey_app/error_player.html")
         return render(request,"hockey_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"hockey_app/search_player.html",{"form":form})
def search_about(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=hockey_db.objects.get(name__iexact=name) 
         except hockey_db.DoesNotExist:
             return render(request,"hockey_app/error_about.html")
         return render(request,"hockey_app/result_about.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"hockey_app/search_about.html",{"form":form})   


