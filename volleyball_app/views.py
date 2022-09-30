from django.shortcuts import render
from volleyball_app.models import volleyball_db
from volleyball_app.forms import playerform
from volleyball_app.forms import aboutform
from volleyball_app.forms import detailsform
from volleyball_app.forms import pointstatsform
from volleyball_app.forms import searchform
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"volleyball_app/home.html")
def player(request):
    players_list=volleyball_db.objects.order_by("name")
    volleyball_dict={"player":players_list}
    return render(request,"volleyball_app/player.html",context=volleyball_dict)	
def about(request):
    players_list=volleyball_db.objects.order_by("name")
    volleyball_dict={"player":players_list}
    return render(request,"volleyball_app/about.html",context=volleyball_dict)			
def details(request):
    players_list=volleyball_db.objects.order_by("name")
    volleyball_dict={"player":players_list}
    return render(request,"volleyball_app/details.html",context=volleyball_dict)	
def pointstats(request):
    players_list=volleyball_db.objects.order_by("name")
    volleyball_dict={"player":players_list}
    return render(request,"volleyball_app/pointstats.html",context=volleyball_dict)			
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
         obj,created=volleyball_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"volleyball_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"volleyball_app/form_player.html",{"form":form})    
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         gender=form.cleaned_data["gender"]
         rank=form.cleaned_data["rank"]
         defaults={"gender":gender,"rank":rank}
         obj,created=volleyball_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"volleyball_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"volleyball_app/form_about.html",{"form":form})
def form_details(request):
    form=detailsform()
    if request.method=="POST":
      form=detailsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         gender=form.cleaned_data["gender"]
         rank=form.cleaned_data["rank"]
         defaults={"gender":gender,"rank":rank}
         obj,created=volleyball_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"volleyball_app/submit_details.html")
      else:
         print("error form invalid")      
    return render(request,"volleyball_app/form_details.html",{"form":form})  
def form_pointstats(request):
    form=pointstatsform()
    if request.method=="POST":
      form=pointstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         points=form.cleaned_data["points"]
         defaults={"points":points}
         obj,created=volleyball_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"volleyball_app/submit_pointstats.html")
      else:
         print("error form invalid")      
    return render(request,"volleyball_app/form_pointstats.html",{"form":form}) 
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=volleyball_db.objects.get(name__iexact=name) 
         except volleyball_db.DoesNotExist:
             return render(request,"volleyball_app/error_player.html")
         return render(request,"volleyball_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"volleyball_app/search_player.html",{"form":form})
def search_about(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=volleyball_db.objects.get(name__iexact=name) 
         except volleyball_db.DoesNotExist:
             return render(request,"volleyball_app/error_about.html")
         return render(request,"volleyball_app/result_about.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"volleyball_app/search_about.html",{"form":form})
def search_details(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=volleyball_db.objects.get(name__iexact=name) 
         except volleyball_db.DoesNotExist:
             return render(request,"volleyball_app/error_details.html")
         return render(request,"volleyball_app/result_details.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"volleyball_app/search_details.html",{"form":form})
def search_pointstats(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=volleyball_db.objects.get(name__iexact=name) 
         except volleyball_db.DoesNotExist:
             return render(request,"volleyball_app/error_pointstats.html")
         return render(request,"volleyball_app/result_pointstats.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"volleyball_app/search_pointstats.html",{"form":form})





































