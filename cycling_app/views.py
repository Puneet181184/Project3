from django.shortcuts import render
from cycling_app.models import cycling_db
from cycling_app.forms import playerform
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"cycling_app/home.html")
def player(request):
    players_list=cycling_db.objects.order_by("name")
    cycling_dict={"player":players_list}
    return render(request,"cycling_app/player.html",context=cycling_dict)		
def about(request):
    players_list=cycling_db.objects.order_by("name")
    cycling_dict={"player":players_list}
    return render(request,"cycling_app/about.html",context=cycling_dict)		    
def details(request):
    players_list=cycling_db.objects.order_by("name")
    cycling_dict={"player":players_list}
    return render(request,"cycling_app/details.html",context=cycling_dict)		    
def gamestats(request):
    players_list=cycling_db.objects.order_by("name")
    cycling_dict={"player":players_list}
    return render(request,"cycling_app/gamestats.html",context=cycling_dict)	
def pointstats(request):
    players_list=cycling_db.objects.order_by("name")
    cycling_dict={"player":players_list}
    return render(request,"cycling_app/pointstats.html",context=cycling_dict)
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
         obj,created=cycling_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"cycling_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"cycling_app/form_player.html",{"form":form})    