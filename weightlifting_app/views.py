from django.shortcuts import render
from weightlifting_app.models import weightlifting_db
from weightlifting_app.forms import playerform
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"weightlifting_app/home.html")
def player(request):
    players_list=weightlifting_db.objects.order_by("name")
    weightlifting_dict={"player":players_list}
    return render(request,"weightlifting_app/player.html",context=weightlifting_dict)		
def about(request):
    players_list=weightlifting_db.objects.order_by("name")
    weightlifting_dict={"player":players_list}
    return render(request,"weightlifting_app/about.html",context=weightlifting_dict)       
def details(request):
    players_list=weightlifting_db.objects.order_by("name")
    weightlifting_dict={"player":players_list}
    return render(request,"weightlifting_app/details.html",context=weightlifting_dict)       
def careerstats(request):
    players_list=weightlifting_db.objects.order_by("name")
    weightlifting_dict={"player":players_list}
    return render(request,"weightlifting_app/careerstats.html",context=weightlifting_dict)       
def matchstats(request):
    players_list=weightlifting_db.objects.order_by("name")
    weightlifting_dict={"player":players_list}
    return render(request,"weightlifting_app/matchstats.html",context=weightlifting_dict)       
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
         obj,created=weightlifting_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"weightlifting_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"weightlifting_app/form_player.html",{"form":form})     
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
         obj,created=weightlifting_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"weightlifting_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"weightlifting_app/form_about.html",{"form":form})     
def form_details(request):
    form=detailsform()
    if request.method=="POST":
      form=detailsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         category=form.cleaned_data["category"]
         rank=form.cleaned_data["rank"]
         defaults={"category":category,"rank":rank}
         obj,created=weightlifting_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"weightlifting_app/submit_details.html")
      else:
         print("error form invalid")      
    return render(request,"weightlifting_app/form_details.html",{"form":form}) 
def form_careersstats(request):
    form=careerstatsform()
    if request.method=="POST":
      form=careerstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         snatch=form.cleaned_data["snatch"]
         jerk=form.cleaned_data["jerk"]
         defaults={"snatch":snatch,"jerk":jerk}
         obj,created=weightlifting_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"weightlifting_app/submit_careerstats.html")
      else:
         print("error form invalid")      
    return render(request,"weightlifting_app/form_careerstats.html",{"form":form})   
def form_matchstats(request):
    form=matchstatsform()
    if request.method=="POST":
      form=matchstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         total=form.cleaned_data["total"]
         defaults={"total":total}
         obj,created=weightlifting_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"weightlifting_app/submit_matchstats.html")
      else:
         print("error form invalid")      
    return render(request,"weightlifting_app/form_matchstats.html",{"form":form})                           