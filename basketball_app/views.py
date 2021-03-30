from django.shortcuts import render
from basketball_app.models import basketball_db
from basketball_app.forms import playerform

# Create your views here.
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"basketball_app/home.html")
def player(request):
    players_list=basketball_db.objects.order_by("name")
    basketball_dict={"player":players_list}
    return render(request,"basketball_app/player.html",context=basketball_dict)		
def about(request):
    players_list=basketball_db.objects.order_by("name")
    basketball_dict={"player":players_list}
    return render(request,"basketball_app/about.html",context=basketball_dict)
def details(request):
    players_list=basketball_db.objects.order_by("name")
    basketball_dict={"player":players_list}
    return render(request,"basketball_app/details.html",context=basketball_dict)
def gamestats(request):
    players_list=basketball_db.objects.order_by("name")
    basketball_dict={"player":players_list}
    return render(request,"basketball_app/gamestats.html",context=basketball_dict)
def goalstats(request):
    players_list=basketball_db.objects.order_by("name")
    basketball_dict={"player":players_list}
    return render(request,"basketball_app/goalstats.html",context=basketball_dict)
def pointstats(request):
    players_list=basketball_db.objects.order_by("name")
    basketball_dict={"player":players_list}
    return render(request,"basketball_app/pointstats.html",context=basketball_dict)
def blockstats(request):
    players_list=basketball_db.objects.order_by("name")
    basketball_dict={"player":players_list}
    return render(request,"basketball_app/blockstats.html",context=basketball_dict)

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
         obj,created=basketball_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"basketball_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"basketball_app/form_player.html",{"form":form})     		






