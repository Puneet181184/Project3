from django.shortcuts import render
from surfing_app.models import surfing_db
from surfing_app.forms import playerform
from surfing_app.forms import aboutform
from surfing_app.forms import detailsform
from surfing_app.forms import pointstatsform
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"surfing_app/home.html")
def player(request):
    players_list=surfing_db.objects.order_by("name")
    surfing_dict={"player":players_list}
    return render(request,"surfing_app/player.html",context=surfing_dict)	
def about(request):
    players_list=surfing_db.objects.order_by("name")
    surfing_dict={"about":players_list}
    return render(request,"surfing_app/about.html",context=surfing_dict) 
def details(request):
    players_list=surfing_db.objects.order_by("name")
    surfing_dict={"details":players_list}
    return render(request,"surfing_app/details.html",context=surfing_dict) 
def pointstats(request):
    players_list=surfing_db.objects.order_by("name")
    surfing_dict={"pointstats":players_list}
    return render(request,"surfing_app/pointstats.html",context=surfing_dict)          
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
         obj,created=surfing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"surfing_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"surfing_app/form_player.html",{"form":form})
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         gender=form.cleaned_data["gender"]
         height=form.cleaned_data["height"]
         weight=form.cleaned_data["weight"]
         defaults={"gender":gender,"height":height,"weight":weight}
         obj,created=surfing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"surfing_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"surfing_app/form_about.html",{"form":form}) 
def form_details(request):
    form=detailsform()
    if request.method=="POST":
      form=detailsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         rank=form.cleaned_data["rank"]
         debut=form.cleaned_data["debut"]
         defaults={"rank":rank,"debut":debut}
         obj,created=surfing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"surfing_app/submit_detailshtml")
      else:
         print("error form invalid")      
    return render(request,"surfing_app/form_details.html",{"form":form})  
def form_pointstats(request):
    form=pointstatsform()
    if request.method=="POST":
      form=pointstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         wins=form.cleaned_data["wins"]
         score=form.cleaned_data["score"]
         defaults={"wins":wins,"score":score}
         obj,created=surfing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"surfing_app/submit_pointstats.html")
      else:
         print("error form invalid")      
    return render(request,"surfing_app/form_pointstats.html",{"form":form})  
