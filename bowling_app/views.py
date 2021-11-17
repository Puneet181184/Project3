from django.shortcuts import render
from bowling_app.models import bowling_db
from bowling_app.forms import playerform
from bowling_app.forms import aboutform
from bowling_app.forms import detailsform
from bowling_app.forms import careerstatsform
from bowling_app.forms import matchstatsform
from bowling_app.forms import titlestatsform
from bowling_app.forms import searchform

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
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         gender=form.cleaned_data["gender"]
         city=form.cleaned_data["city"]
         state=form.cleaned_data["state"]
         defaults={"gender":gender,"city":city,"state":state}
         obj,created=bowling_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"bowling_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"bowling_app/form_about.html",{"form":form})
def form_details(request):
    form=detailsform()
    if request.method=="POST":
      form=detailsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         debut=form.cleaned_data["debut"]
         defaults={"debut":debut}
         obj,created=bowling_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"bowling_app/submit_details.html")
      else:
         print("error form invalid")      
    return render(request,"bowling_app/form_details.html",{"form":form}) 
def form_careerstats(request):
    form=careerstatsform()
    if request.method=="POST":
      form=careerstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         bowls=form.cleaned_data["bowls"]
         events=form.cleaned_data["events"]
         championships=form.cleaned_data["championships"]
         defaults={"bowls":bowls,"events":events,"championships":championships}
         obj,created=bowling_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"bowling_app/submit_careerstats.html")
      else:
         print("error form invalid")      
    return render(request,"bowling_app/form_careerstats.html",{"form":form})
def form_matchstats(request):
    form=matchstatsform()
    if request.method=="POST":
      form=matchstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         matches=form.cleaned_data["matches"]
         cashes=form.cleaned_data["cashes"]
         defaults={"matches":matches,"cashes":cashes}
         obj,created=bowling_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"bowling_app/submit_matchstats.html")
      else:
         print("error form invalid")      
    return render(request,"bowling_app/form_matchstats.html",{"form":form})
def form_titlestats(request):
    form=titlestatsform()
    if request.method=="POST":
      form=titlestatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         titles=form.cleaned_data["titles"]
         average=form.cleaned_data["average"]
         defaults={"titles":titles,"average":average}
         obj,created=bowling_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"bowling_app/submit_titlestats.html")
      else:
         print("error form invalid")      
    return render(request,"bowling_app/form_titlestats.html",{"form":form})    
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=bowling_db.objects.get(name__iexact=name) 
         except bowling_db.DoesNotExist:
             return render(request,"bowling_app/error_player.html")
         return render(request,"bowling_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"bowling_app/search_player.html",{"form":form})








