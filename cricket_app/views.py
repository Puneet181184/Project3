from django.shortcuts import render
from cricket_app.models import cricket_db
from cricket_app.forms import playerform
# Create your views here.
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"cricket_app/home.html")
def player(request):
    players_list=cricket_db.objects.order_by("name")
    cricket_dict={"player":players_list}
    return render(request,"cricket_app/player.html",context=cricket_dict)		
def about(request):
    players_list=cricket_db.objects.order_by("name")
    cricket_dict={"player":players_list}
    return render(request,"cricket_app/about.html",context=cricket_dict)	
def odistats(request):
    players_list=cricket_db.objects.order_by("name")
    cricket_dict={"player":players_list}
    return render(request,"cricket_app/odistats.html",context=cricket_dict)	
def teststats(request):
    players_list=cricket_db.objects.order_by("name")
    cricket_dict={"player":players_list}
    return render(request,"cricket_app/teststats.html",context=cricket_dict)	
def t20stats(request):
    players_list=cricket_db.objects.order_by("name")
    cricket_dict={"player":players_list}
    return render(request,"cricket_app/t20stats.html",context=cricket_dict)	

def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         country=form.cleaned_data["country"]
         defaults={"age":age,"country":country}
         obj,created=cricket_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"cricket_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"cricket_app/form_player.html",{"form":form}) 

def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         debut=form.cleaned_data["debut"]
         skill=form.cleaned_data["skill"]
         defaults={"debut":debut,"skill":skill}
         obj,created=cricket_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"cricket_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"cricket_app/form_about.html",{"form":form})


def form_odistats(request):
    form=odistatsform()
    if request.method=="POST":
      form=odistatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         odimatches=form.cleaned_data["odimatches"]
         odiruns=form.cleaned_data["odiruns"]
         odiwickets=form.cleaned_data["odiwickets"]
         odicatches=form.cleaned_data["odicatches"]
         defaults={"odimatches":odimatches,"odiruns":odiruns,"odiwickets":odiwickets,"odicatches":odicatches}
         obj,created=cricket_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"cricket_app/submit_odistats.html")
      else:
         print("error form invalid")      
    return render(request,"cricket_app/form_odistats.html",{"form":form})       



def form_teststats(request):
    form=teststatsform()
    if request.method=="POST":
      form=teststatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         testmatches=form.cleaned_data["testmatches"]
         testruns=form.cleaned_data["testruns"]
         testwickets=form.cleaned_data["testwickets"]
         testcatches=form.cleaned_data["testcatches"]
         defaults={"testmatches":testmatches,"testruns":testruns,"testwickets":testwickets,"testcatches":testcatches}
         obj,created=cricket_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"cricket_app/submit_teststats.html")
      else:
         print("error form invalid")      
    return render(request,"cricket_app/form_teststats.html",{"form":form})   


def form_t20stats(request):
    form=t20tatsform()
    if request.method=="POST":
      form=t20statsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         t20matches=form.cleaned_data["t20matches"]
         t20runs=form.cleaned_data["t20runs"]
         t20wickets=form.cleaned_data["t20wickets"]
         t20catches=form.cleaned_data["t20catches"]
         defaults={"t20matches":t20matches,"t20runs":t20runs,"t20wickets":t20wickets,"t20catches":t20catches}
         obj,created=cricket_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"cricket_app/submit_t20stats.html")
      else:
         print("error form invalid")      
    return render(request,"cricket_app/form_t20stats.html",{"form":form})                 
