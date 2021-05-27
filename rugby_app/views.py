from django.shortcuts import render
from rugby_app.models import rugby_db
from rugby_app.forms import playerform
# Create your views here.
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"rugby_app/home.html")
def player(request):
    players_list=rugby_db.objects.order_by("name")
    rugby_dict={"player":players_list}
    return render(request,"rugby_app/player.html",context=rugby_dict)			
def about(request):
    players_list=rugby_db.objects.order_by("name")
    rugby_dict={"player":players_list}
    return render(request,"rugby_app/about.html",context=rugby_dict)		
def details(request):
    players_list=rugby_db.objects.order_by("name")
    rugby_dict={"player":players_list}
    return render(request,"rugby_app/details.html",context=rugby_dict)
def matchstats(request):
    players_list=rugby_db.objects.order_by("name")
    rugby_dict={"player":players_list}
    return render(request,"rugby_app/matchstats.html",context=rugby_dict)
def gamestats(request):
    players_list=rugby_db.objects.order_by("name")
    rugby_dict={"player":players_list}
    return render(request,"rugby_app/gamestats.html",context=rugby_dict)
def pointstats(request):
    players_list=rugby_db.objects.order_by("name")
    rugby_dict={"player":players_list}
    return render(request,"rugby_app/pointstats.html",context=rugby_dict)
def cardstats(request):
    players_list=rugby_db.objects.order_by("name")
    rugby_dict={"player":players_list}
    return render(request,"rugby_app/cardstats.html",context=rugby_dict)

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
         obj,created=rugby_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"rugby_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"rugby_app/form_player.html",{"form":form})       	    	    	    	    	