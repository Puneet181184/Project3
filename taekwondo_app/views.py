from django.shortcuts import render
from taekwondo_app.models import taekwondo_db
from taekwondo_app.forms import playerform
from taekwondo_app.forms import aboutform
from taekwondo_app.forms import detailsform
from taekwondo_app.forms import pointstatsform
from taekwondo_app.forms import searchform
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"taekwondo_app/home.html")
def player(request):
    players_list=taekwondo_db.objects.order_by("name")
    taekwondo_dict={"player":players_list}
    return render(request,"taekwondo_app/player.html",context=taekwondo_dict)	
def about(request):
    players_list=taekwondo_db.objects.order_by("name")
    taekwondo_dict={"player":players_list}
    return render(request,"taekwondo_app/about.html",context=taekwondo_dict)	    
def details(request):
    players_list=taekwondo_db.objects.order_by("name")
    taekwondo_dict={"player":players_list}
    return render(request,"taekwondo_app/details.html",context=taekwondo_dict)	
def pointstats(request):
    players_list=taekwondo_db.objects.order_by("name")
    taekwondo_dict={"player":players_list}
    return render(request,"taekwondo_app/pointstats.html",context=taekwondo_dict)	
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
         obj,created=taekwondo_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"taekwondo_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"taekwondo_app/form_player.html",{"form":form})
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         gender=form.cleaned_data["gender"]
         weight=form.cleaned_data["weight"]
         defaults={"gender":gender,"weight":weight}
         obj,created=taekwondo_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"taekwondo_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"taekwondo_app/form_about.html",{"form":form}) 
def form_details(request):
    form=detailsform()
    if request.method=="POST":
      form=detailsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         rank=form.cleaned_data["rank"]
         defaults={"rank":rank}
         obj,created=taekwondo_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"taekwondo_app/submit_details.html")
      else:
         print("error form invalid")      
    return render(request,"taekwondo_app/form_details.html",{"form":form})   
def form_pointstats(request):
    form=pointstatsform()
    if request.method=="POST":
      form=pointstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         points=form.cleaned_data["points"]
         defaults={"points":points}
         obj,created=taekwondo_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"taekwondo_app/submit_pointstats.html")
      else:
         print("error form invalid")      
    return render(request,"taekwondo_app/form_pointstats.html",{"form":form})                 
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=taekwondo_db.objects.get(name__iexact=name) 
         except taekwondo_db.DoesNotExist:
             return render(request,"taekwondo_app/error_player.html")
         return render(request,"taekwondo_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"taekwondo_app/search_player.html",{"form":form})
def search_about(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=taekwondo_db.objects.get(name__iexact=name) 
         except taekwondo_db.DoesNotExist:
             return render(request,"taekwondo_app/error_about.html")
         return render(request,"taekwondo_app/result_about.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"taekwondo_app/search_about.html",{"form":form})  
def search_details(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=taekwondo_db.objects.get(name__iexact=name) 
         except taekwondo_db.DoesNotExist:
             return render(request,"taekwondo_app/error_details.html")
         return render(request,"taekwondo_app/result_details.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"taekwondo_app/search_details.html",{"form":form}) 
def search_pointstats(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=taekwondo_db.objects.get(name__iexact=name) 
         except taekwondo_db.DoesNotExist:
             return render(request,"taekwondo_app/error_pointstats.html")
         return render(request,"taekwondo_app/result_pointstats.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"taekwondo_app/search_pointstats.html",{"form":form})         


