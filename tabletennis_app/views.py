from django.shortcuts import render
from tabletennis_app.models import tabletennis_db
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"tabletennis_app/home.html")
def player(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/player.html",context=tabletennis_dict)			
def about(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/about.html",context=tabletennis_dict) 
def details(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/details.html",context=tabletennis_dict)
def careerstats(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/careerstats.html",context=tabletennis_dict) 
def singlesstats(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/singlesstats.html",context=tabletennis_dict)
def doublesstats(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/doublesstats.html",context=tabletennis_dict)
def totalstats(request):
    players_list=tabletennis_db.objects.order_by("name")
    tabletennis_dict={"player":players_list}
    return render(request,"tabletennis_app/totalstats.html",context=tabletennis_dict)                                                      

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
         obj,created=tabletennis_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"tabletennis_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"tabletennis_app/form_player.html",{"form":form})   