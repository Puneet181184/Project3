from django.shortcuts import render
from baseball_app.models import baseball_db
from baseball_app.forms import playerform
from baseball_app.forms import aboutform
from baseball_app.forms import detailsform
from baseball_app.forms import gamestatsform
from baseball_app.forms import runstatsform
from baseball_app.forms import strikestatsform
from baseball_app.forms import basestatsform
from baseball_app.forms import searchform

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
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         college=form.cleaned_data["college"]
         team=form.cleaned_data["team"]
         position=form.cleaned_data["position"]
         defaults={"college":college,"team":team,"position":position}
         obj,created=baseball_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"baseball_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"baseball_app/form_about.html",{"form":form})   
def form_details(request):
    form=detailsform()
    if request.method=="POST":
      form=detailsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         debut=form.cleaned_data["debut"]
         height=form.cleaned_data["height"]
         weight=form.cleaned_data["weight"]
         defaults={"debut":debut,"height":height,"weight":weight}
         obj,created=baseball_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"baseball_app/submit_details.html")
      else:
         print("error form invalid")      
    return render(request,"baseball_app/form_details.html",{"form":form}) 
def form_gamestats(request):
    form=gamestatsform()
    if request.method=="POST":
      form=gamestatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         games=form.cleaned_data["games"]
         appearances=form.cleaned_data["appearances"]
         atbats=form.cleaned_data["atbats"]
         defaults={"games":games,"appearances":appearances,"atbats":atbats}
         obj,created=baseball_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"baseball_app/submit_gamestats.html")
      else:
         print("error form invalid")      
    return render(request,"baseball_app/form_gamestats.html",{"form":form})     		
def form_runstats(request):
    form=runstatsform()
    if request.method=="POST":
      form=runstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         runs=form.cleaned_data["runs"]
         hits=form.cleaned_data["hits"]
         doubles=form.cleaned_data["doubles"]
         triples=form.cleaned_data["triples"]
         homeruns=form.cleaned_data["homeruns"]
         runsbatted=form.cleaned_data["runsbatted"]
         defaults={"runs":runs,"hits":hits,"doubles":doubles,"triples":triples,"homeruns":homeruns,"runsbatted":runsbatted}
         obj,created=baseball_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"baseball_app/submit_runstats.html")
      else:
         print("error form invalid")      
    return render(request,"baseball_app/form_runstats.html",{"form":form}) 
def form_strikestats(request):
    form=strikestatsform()
    if request.method=="POST":
      form=strikestatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         steals=form.cleaned_data["steals"]
         walks=form.cleaned_data["walks"]
         strikeouts=form.cleaned_data["strikeouts"]
         defaults={"steals":steals,"walks":walks,"strikeouts":strikeouts}
         obj,created=baseball_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"baseball_app/submit_strikestats.html")
      else:
         print("error form invalid")      
    return render(request,"baseball_app/form_strikestats.html",{"form":form})
def form_basestats(request):
    form=basestatsform()
    if request.method=="POST":
      form=basestatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         stolenbases=form.cleaned_data["stolenbases"]
         caughtstealing=form.cleaned_data["caughtstealing"]
         totalbases=form.cleaned_data["totalbases"]
         defaults={"stolenbases":stolenbases,"caughtstealing":caughtstealing,"totalbases":totalbases}
         obj,created=baseball_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"baseball_app/submit_basestats.html")
      else:
         print("error form invalid")      
    return render(request,"baseball_app/form_basestats.html",{"form":form})   

def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=baseball_db.objects.get(name__iexact=name) 
         except baseball_db.DoesNotExist:
             return render(request,"baseball_app/error_player.html")
         return render(request,"baseball_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"baseball_app/search_player.html",{"form":form})
def search_about(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=baseball_db.objects.get(name__iexact=name) 
         except baseball_db.DoesNotExist:
             return render(request,"baseball_app/error_about.html")
         return render(request,"baseball_app/result_about.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"baseball_app/search_about.html",{"form":form}) 
def search_details(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=baseball_db.objects.get(name__iexact=name) 
         except baseball_db.DoesNotExist:
             return render(request,"baseball_app/error_details.html")
         return render(request,"baseball_app/result_details.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"baseball_app/search_details.html",{"form":form}) 
def search_gamestats(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=baseball_db.objects.get(name__iexact=name) 
         except baseball_db.DoesNotExist:
             return render(request,"baseball_app/error_gamestats.html")
         return render(request,"baseball_app/result_gamestats.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"baseball_app/search_gamestats.html",{"form":form}) 
def search_runstats(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=baseball_db.objects.get(name__iexact=name) 
         except baseball_db.DoesNotExist:
             return render(request,"baseball_app/error_runstats.html")
         return render(request,"baseball_app/result_runstats.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"baseball_app/search_runstats.html",{"form":form}) 
def search_strikestats(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=baseball_db.objects.get(name__iexact=name) 
         except baseball_db.DoesNotExist:
             return render(request,"baseball_app/error_strikestats.html")
         return render(request,"baseball_app/result_strikestats.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"baseball_app/search_strikestats.html",{"form":form})    
def search_basestats(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=baseball_db.objects.get(name__iexact=name) 
         except baseball_db.DoesNotExist:
             return render(request,"baseball_app/error_basestats.html")
         return render(request,"baseball_app/result_basestats.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"baseball_app/search_basestats.html",{"form":form})    

















    		    		    		    		    		    		




    		    		    		    		    		    		
    		    		    		    		    		    		


