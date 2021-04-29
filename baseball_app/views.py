from django.shortcuts import render
from baseball_app.models import baseball_db
from baseball_app.forms import playerform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"baseball_app/home.html")
def player(request):
    players_list=baseball_db.objects.order_by("name")
    baseball_dict={"player":players_list}
    return render(request,"baseball_app/player.html",context=baseball_dict)			
def about(request):
    players_list=baseball_db.objects.order_by("name")
    baseball_dict={"player":players_list}
    return render(request,"baseball_app/about.html",context=baseball_dict)
def details(request):
    players_list=baseball_db.objects.order_by("name")
    baseball_dict={"player":players_list}
    return render(request,"baseball_app/details.html",context=baseball_dict)
def gamestats(request):
    players_list=baseball_db.objects.order_by("name")
    baseball_dict={"player":players_list}
    return render(request,"baseball_app/gamestats.html",context=baseball_dict)
def runstats(request):
    players_list=baseball_db.objects.order_by("name")
    baseball_dict={"player":players_list}
    return render(request,"baseball_app/runstats.html",context=baseball_dict)
def strikestats(request):
    players_list=baseball_db.objects.order_by("name")
    baseball_dict={"player":players_list}
    return render(request,"baseball_app/strikestats.html",context=baseball_dict)
def basestats(request):
    players_list=baseball_db.objects.order_by("name")
    baseball_dict={"player":players_list}
    return render(request,"baseball_app/basestats.html",context=baseball_dict)
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         dob=form.cleaned_data["dob"]
         nationality=form.cleaned_data["nationality"]
         defaults={"age":age,"dob":dob,"nationality":nationality}
         obj,created=baseball_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"baseball_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"baseball_app/form_player.html",{"form":form})     		

    		    		    		    		    		    		


