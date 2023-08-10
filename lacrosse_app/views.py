from django.shortcuts import render
from lacrosse_app.models import lacrosse_db
from lacrosse_app.forms import playerform
from lacrosse_app.forms import aboutform
from lacrosse_app.forms import pointstatsform
from lacrosse_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"lacrosse_app/home.html")
def player(request):
    players_list=lacrosse_db.objects.order_by("name")
    lacrosse_dict={"player":players_list}
    return render(request,"lacrosse_app/player.html",context=lacrosse_dict)		
def about(request):
    players_list=lacrosse_db.objects.order_by("name")
    lacrosse_dict={"player":players_list}
    return render(request,"lacrosse_app/about.html",context=lacrosse_dict)     
def pointstats(request):
    players_list=lacrosse_db.objects.order_by("name")
    lacrosse_dict={"player":players_list}
    return render(request,"lacrosse_app/pointstats.html",context=lacrosse_dict)         
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         country=form.cleaned_data["country"]
         defaults={"age":age,"country":country}
         obj,created=lacrosse_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"lacrosse_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"lacrosse_app/form_player.html",{"form":form})           
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         height=form.cleaned_data["height"]
         weight=form.cleaned_data["weight"]
         defaults={"height":height,"weight":weight}
         obj,created=lacrosse_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"lacrosse_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"lacrosse_app/form_about.html",{"form":form})    
def form_pointstats(request):
    form=pointstatsform()
    if request.method=="POST":
      form=pointstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         rank=form.cleaned_data["rank"]
         defaults={"rank":rank}
         obj,created=lacrosse_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"lacrosse_app/submit_pointstats.html")
      else:
         print("error form invalid")      
    return render(request,"lacrosse_app/form_pointstats.html",{"form":form})               
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=lacrosse_db.objects.get(name__iexact=name) 
         except lacrosse_db.DoesNotExist:
             return render(request,"lacrosse_app/error_player.html")
         return render(request,"lacrosse_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"lacrosse_app/search_player.html",{"form":form}) 
def search_about(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=lacrosse_db.objects.get(name__iexact=name) 
         except lacrosse_db.DoesNotExist:
             return render(request,"lacrosse_app/error_about.html")
         return render(request,"lacrosse_app/result_about.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"lacrosse_app/search_about.html",{"form":form}) 
def search_pointstats(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=lacrosse_db.objects.get(name__iexact=name) 
         except lacrosse_db.DoesNotExist:
             return render(request,"lacrosse_app/error_pointstats.html")
         return render(request,"lacrosse_app/result_pointstats.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"lacrosse_app/search_pointstats.html",{"form":form})     
