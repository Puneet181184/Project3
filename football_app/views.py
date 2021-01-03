from django.shortcuts import render
from football_app.models import football_db
from football_app.forms import playerform


def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"football_app/home.html")
def player(request):
    players_list=football_db.objects.order_by("name")
    football_dict={"player":players_list}
    return render(request,"football_app/player.html",context=football_dict)		
def about(request):
    players_list=football_db.objects.order_by("name")
    football_dict={"player":players_list}
    return render(request,"football_app/about.html",context=football_dict)
def details(request):
    players_list=football_db.objects.order_by("name")
    football_dict={"player":players_list}
    return render(request,"football_app/details.html",context=football_dict)
def matchstats(request):
    players_list=football_db.objects.order_by("name")
    football_dict={"player":players_list}
    return render(request,"football_app/matchstats.html",context=football_dict)
def goalstats(request):
    players_list=football_db.objects.order_by("name")
    football_dict={"player":players_list}
    return render(request,"football_app/goalstats.html",context=football_dict)
def penaltystats(request):
    players_list=football_db.objects.order_by("name")
    football_dict={"player":players_list}
    return render(request,"football_app/penaltystats.html",context=football_dict)
def cardstats(request):
    players_list=football_db.objects.order_by("name")
    football_dict={"player":players_list}
    return render(request,"football_app/cardstats.html",context=football_dict)

def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         dob=form.cleaned_data["dob"]
         nationality=form.cleaned_data["nationality"]
         birthplace=form.cleaned_data["birthplace"]
         defaults={"age":age,"dob":dob,"nationality":nationality,"birthplace":birthplace}
         obj,created=football_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"football_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"football_app/form_player.html",{"form":form}) 



    		







