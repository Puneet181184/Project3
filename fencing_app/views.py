from django.shortcuts import render
from fencing_app.models import fencing_db
from fencing_app.forms import playerform
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"fencing_app/home.html")
def player(request):
    players_list=fencing_db.objects.order_by("name")
    fencing_dict={"player":players_list}
    return render(request,"fencing_app/player.html",context=fencing_dict)		
def about(request):
    players_list=fencing_db.objects.order_by("name")
    fencing_dict={"player":players_list}
    return render(request,"fencing_app/about.html",context=fencing_dict)
def details(request):
    players_list=fencing_db.objects.order_by("name")
    fencing_dict={"player":players_list}
    return render(request,"fencing_app/details.html",context=fencing_dict)	
def gamestats(request):
    players_list=fencing_db.objects.order_by("name")
    fencing_dict={"player":players_list}
    return render(request,"fencing_app/gamestats.html",context=fencing_dict)
def pointstats(request):
    players_list=fencing_db.objects.order_by("name")
    fencing_dict={"player":players_list}
    return render(request,"fencing_app/pointstats.html",context=fencing_dict)		    		    	    
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
         obj,created=fencing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"fencing_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"fencing_app/form_player.html",{"form":form})   