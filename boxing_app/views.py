from django.shortcuts import render
from boxing_app.models import boxing_db
from boxing_app.forms import playerform
from boxing_app.forms import aboutform
from boxing_app.forms import pointstatsform
from boxing_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"boxing_app/home.html")
def player(request):
    players_list=boxing_db.objects.order_by("name")
    boxing_dict={"player":players_list}
    return render(request,"boxing_app/player.html",context=boxing_dict)			
def about(request):
    players_list=boxing_db.objects.order_by("name")
    boxing_dict={"player":players_list}
    return render(request,"boxing_app/about.html",context=boxing_dict)		
def pointstats(request):
    players_list=boxing_db.objects.order_by("name")
    boxing_dict={"player":players_list}
    return render(request,"boxing_app/pointstats.html",context=boxing_dict)		
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         country=form.cleaned_data["country"]
         defaults={"age":age,"country":country}
         obj,created=boxing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"boxing_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"boxing_app/form_player.html",{"form":form})         
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         height=form.cleaned_data["height"]
         weight=form.cleaned_data["weight"]
         defaults={"height":height,"weight":weight}
         obj,created=boxing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"boxing_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"boxing_app/form_about.html",{"form":form})             
def form_pointstats(request):
    form=pointstatsform()
    if request.method=="POST":
      form=pointstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         wins=form.cleaned_data["wins"]
         losses=form.cleaned_data["losses"]
         draws=form.cleaned_data["draws"]
         defaults={"wins":wins,"losses":losses,"draws":draws}
         obj,created=boxing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"boxing_app/submit_pointstats.html")
      else:
         print("error form invalid")      
    return render(request,"boxing_app/form_pointstats.html",{"form":form})             
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=boxing_db.objects.get(name__iexact=name) 
         except boxing_db.DoesNotExist:
             return render(request,"boxing_app/error_player.html")
         return render(request,"boxing_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"boxing_app/search_player.html",{"form":form})  
def search_about(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=boxing_db.objects.get(name__iexact=name) 
         except boxing_db.DoesNotExist:
             return render(request,"boxing_app/error_about.html")
         return render(request,"boxing_app/result_about.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"boxing_app/search_about.html",{"form":form}) 
def search_pointstats(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=boxing_db.objects.get(name__iexact=name) 
         except boxing_db.DoesNotExist:
             return render(request,"boxing_app/error_pointstats.html")
         return render(request,"boxing_app/result_pointstats.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"boxing_app/search_pointstats.html",{"form":form})           
