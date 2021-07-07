from django.shortcuts import render
from icehockey_app.models import icehockey_db
from icehockey_app.forms import playerform
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"icehockey_app/home.html")
def player(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/player.html",context=icehockey_dict)		
def about(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/about.html",context=icehockey_dict)       
def details(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/details.html",context=icehockey_dict) 
def gamestats(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/gamestats.html",context=icehockey_dict)
def goalstats(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/goalstats.html",context=icehockey_dict)
def pointstats(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/pointstats.html",context=icehockey_dict)
def shotstats(request):
    players_list=icehockey_db.objects.order_by("name")
    icehockey_dict={"player":players_list}
    return render(request,"icehockey_app/shotstats.html",context=icehockey_dict)       
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
         obj,created=icehockey_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"icehockey_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"icehockey_app/form_player.html",{"form":form})










