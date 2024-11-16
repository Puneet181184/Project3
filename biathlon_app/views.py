from django.shortcuts import render
from biathlon_app.models import biathlon_db
from biathlon_app.forms import playerform
from biathlon_app.forms import aboutform
from biathlon_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"biathlon_app/home.html")
def player(request):
    players_list=biathlon_db.objects.order_by("name")
    biathlon_dict={"player":players_list}
    return render(request,"biathlon_app/player.html",context=biathlon_dict)		
def about(request):
    players_list=biathlon_db.objects.order_by("name")
    biathlon_dict={"player":players_list}
    return render(request,"biathlon_app/about.html",context=biathlon_dict)	
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         dob=form.cleaned_data["dob"]
         country=form.cleaned_data["country"]
         defaults={"dob":dob,"country":country}
         obj,created=biathlon_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"biathlon_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"biathlon_app/form_player.html",{"form":form})     
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         gender=form.cleaned_data["gender"]
         rank=form.cleaned_data["rank"]
         points=form.cleaned_data["points"]
         defaults={"gender":gender,"rank":rank,"points":points}
         obj,created=biathlon_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"biathlon_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"biathlon_app/form_about.html",{"form":form})     
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=biathlon_db.objects.get(name__iexact=name) 
         except biathlon_db.DoesNotExist:
             return render(request,"biathlon_app/error_player.html")
         return render(request,"biathlon_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"biathlon_app/search_player.html",{"form":form})
def search_about(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=biathlon_db.objects.get(name__iexact=name) 
         except archery_db.DoesNotExist:
             return render(request,"biathlon_app/error_about.html")
         return render(request,"biathlon_app/result_about.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"biathlon_app/search_about.html",{"form":form})    