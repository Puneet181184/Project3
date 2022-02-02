from django.shortcuts import render
from pool_app.models import pool_db
from pool_app.forms import playerform
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"pool_app/home.html")
def player(request):
    players_list=pool_db.objects.order_by("name")
    pool_dict={"player":players_list}
    return render(request,"pool_app/player.html",context=pool_dict)		
def about(request):
    players_list=pool_db.objects.order_by("name")
    pool_dict={"player":players_list}
    return render(request,"pool_app/about.html",context=pool_dict)
def details(request):
    players_list=pool_db.objects.order_by("name")
    pool_dict={"player":players_list}
    return render(request,"pool_app/details.html",context=pool_dict)
def pointstats(request):
    players_list=pool_db.objects.order_by("name")
    pool_dict={"player":players_list}
    return render(request,"pool_app/pointstats.html",context=pool_dict)	
def careerstats(request):
    players_list=pool_db.objects.order_by("name")
    pool_dict={"player":players_list}
    return render(request,"pool_app/careerstats.html",context=pool_dict)
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
         obj,created=pool_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"pool_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"pool_app/form_player.html",{"form":form})     		    	    		    		    