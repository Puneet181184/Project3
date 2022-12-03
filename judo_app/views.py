from django.shortcuts import render
from judo_app.models import judo_db
from judo_app.forms import playerform
from judo_app.forms import aboutform
from judo_app.forms import pointstatsform
from judo_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"judo_app/home.html")
def player(request):
    players_list=judo_db.objects.order_by("name")
    judo_dict={"player":players_list}
    return render(request,"judo_app/player.html",context=judo_dict)	
def about(request):
    players_list=judo_db.objects.order_by("name")
    judo_dict={"player":players_list}
    return render(request,"judo_app/about.html",context=judo_dict)	
def pointstats(request):
    players_list=judo_db.objects.order_by("name")
    judo_dict={"player":players_list}
    return render(request,"judo_app/pointstats.html",context=judo_dict)	
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         country=form.cleaned_data["country"]
         defaults={"age":age,"country":country}
         obj,created=judo_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"judo_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"judo_app/form_player.html",{"form":form})                
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         rank=form.cleaned_data["rank"]
         defaults={"rank":rank}
         obj,created=judo_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"judo_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"judo_app/form_about.html",{"form":form})  
def form_pointstats(request):
    form=pointstatsform()
    if request.method=="POST":
      form=pointstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         points=form.cleaned_data["points"]
         gold=form.cleaned_data["gold"]
         silver=form.cleaned_data["silver"]
         bronze=form.cleaned_data["bronze"]
         defaults={"points":points,"gold":gold,"silver":silver,"bronze":bronze}
         obj,created=judo_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"judo_app/submit_pointstats.html")
      else:
         print("error form invalid")      
    return render(request,"judo_app/form_pointstats.html",{"form":form})  
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=judo_db.objects.get(name__iexact=name) 
         except judo_db.DoesNotExist:
             return render(request,"judo_app/error_player.html")
         return render(request,"judo_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"judo_app/search_player.html",{"form":form}) 
def search_about(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=judo_db.objects.get(name__iexact=name) 
         except judo_db.DoesNotExist:
             return render(request,"judo_app/error_about.html")
         return render(request,"judo_app/result_about.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"judo_app/search_about.html",{"form":form})
def search_pointstats(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=judo_db.objects.get(name__iexact=name) 
         except judo_db.DoesNotExist:
             return render(request,"judo_app/error_pointstats.html")
         return render(request,"judo_app/result_pointstats.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"judo_app/search_pointstats.html",{"form":form})                                               