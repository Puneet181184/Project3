from django.shortcuts import render
from bowling_app.models import bowling_db
from bowling_app.forms import playerform
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"bowling_app/home.html")
def player(request):
    players_list=bowling_db.objects.order_by("name")
    bowling_dict={"player":players_list}
    return render(request,"bowling_app/player.html",context=bowling_dict)		
def about(request):
    players_list=bowling_db.objects.order_by("name")
    bowling_dict={"player":players_list}
    return render(request,"bowling_app/about.html",context=bowling_dict) 
def details(request):
    players_list=bowling_db.objects.order_by("name")
    bowling_dict={"player":players_list}
    return render(request,"bowling_app/details.html",context=bowling_dict)       
def careerstats(request):
    players_list=bowling_db.objects.order_by("name")
    bowling_dict={"player":players_list}
    return render(request,"bowling_app/careerstats.html",context=bowling_dict)       
def matchstats(request):
    players_list=bowling_db.objects.order_by("name")
    bowling_dict={"player":players_list}
    return render(request,"bowling_app/matchstats.html",context=bowling_dict)
def titlestats(request):
    players_list=bowling_db.objects.order_by("name")
    bowling_dict={"player":players_list}
    return render(request,"bowling_app/titlestats.html",context=bowling_dict)       
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         country=form.cleaned_data["country"]
         defaults={"age":age,"country":country}
         obj,created=bowling_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"bowling_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"bowling_app/form_player.html",{"form":form})   

