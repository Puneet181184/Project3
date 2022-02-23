from django.shortcuts import render
from archery_app.models import archery_db
from archery_app.forms import playerform
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"archery_app/home.html")
def player(request):
    players_list=archery_db.objects.order_by("name")
    archery_dict={"player":players_list}
    return render(request,"archery_app/player.html",context=archery_dict)		
def about(request):
    players_list=archery_db.objects.order_by("name")
    archery_dict={"player":players_list}
    return render(request,"archery_app/about.html",context=archery_dict)		    
def details(request):
    players_list=archery_db.objects.order_by("name")
    archery_dict={"player":players_list}
    return render(request,"archery_app/details.html",context=archery_dict)		    
def gamestats(request):
    players_list=archery_db.objects.order_by("name")
    archery_dict={"player":players_list}
    return render(request,"archery_app/gamestats.html",context=archery_dict)	
def pointstats(request):
    players_list=archery_db.objects.order_by("name")
    archery_dict={"player":players_list}
    return render(request,"archery_app/pointstats.html",context=archery_dict)
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
         obj,created=archery_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"archery_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"archery_app/form_player.html",{"form":form})     
    		    	    