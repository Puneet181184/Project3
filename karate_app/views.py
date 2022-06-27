from django.shortcuts import render
from karate_app.models import karate_db
from karate_app.forms import playerform
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"karate_app/home.html")
def player(request):
    players_list=karate_db.objects.order_by("name")
    karate_dict={"player":players_list}
    return render(request,"karate_app/player.html",context=karate_dict)		
def about(request):
    players_list=karate_db.objects.order_by("name")
    karate_dict={"player":players_list}
    return render(request,"karate_app/about.html",context=karate_dict)	
def details(request):
    players_list=karate_db.objects.order_by("name")
    karate_dict={"player":players_list}
    return render(request,"karate_app/details.html",context=karate_dict)
def pointstats(request):
    players_list=karate_db.objects.order_by("name")
    karate_dict={"player":players_list}
    return render(request,"karate_app/pointstats.html",context=karate_dict)	
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         country=form.cleaned_data["country"]
         defaults={"age":age,"country":country}
         obj,created=karate_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"karate_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"karate_app/form_player.html",{"form":form})    	    		    	    