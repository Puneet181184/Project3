from django.shortcuts import render
from pool_app.models import pool_db
from pool_app.forms import playerform
from pool_app.forms import aboutform
from pool_app.forms import detailsform
from pool_app.forms import pointstatsform
from pool_app.forms import careerstatsform
from pool_app.forms import searchform
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"pool_app/home.html")
def player(request):
    players_list=pool_db.objects.order_by("name")
    pool_dict={"player":players_list}
    return render(request,"pool_app/player.html",context=pool_dict)		
def about(request):
    players_list=pool_db.objects.order_by("name")
    pool_dict={"player":players_list}
    return render(request,"pool_app/about.html",context=pool_dict)
def details(request):
    players_list=pool_db.objects.order_by("name")
    pool_dict={"player":players_list}
    return render(request,"pool_app/details.html",context=pool_dict)
def pointstats(request):
    players_list=pool_db.objects.order_by("name")
    pool_dict={"player":players_list}
    return render(request,"pool_app/pointstats.html",context=pool_dict)	
def careerstats(request):
    players_list=pool_db.objects.order_by("name")
    pool_dict={"player":players_list}
    return render(request,"pool_app/careerstats.html",context=pool_dict)
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
         obj,created=pool_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"pool_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"pool_app/form_player.html",{"form":form})  
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         gender=form.cleaned_data["gender"]
         defaults={"gender":gender}
         obj,created=pool_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"pool_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"pool_app/form_about.html",{"form":form}) 
def form_details(request):
    form=detailsform()
    if request.method=="POST":
      form=detailsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         rank=form.cleaned_data["rank"]
         wpanumber=form.cleaned_data["wpanumber"]
         defaults={"rank":rank,"wpanumber":wpanumber}
         obj,created=pool_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"pool_app/submit_details.html")
      else:
         print("error form invalid")      
    return render(request,"pool_app/form_details.html",{"form":form})  
def form_pointstats(request):
    form=pointstatsform()
    if request.method=="POST":
      form=pointstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         usopenpoints=form.cleaned_data["usopenpoints"]
         austriaopenpoints=form.cleaned_data["austriaopenpoints"]
         defaults={"usopenpoints":usopenpoints,"austriaopenpoints":austriaopenpoints}
         obj,created=pool_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"pool_app/submit_pointstats.html")
      else:
         print("error form invalid")      
    return render(request,"pool_app/form_pointstats.html",{"form":form}) 
def form_careerstats(request):
    form=careerstatsform()
    if request.method=="POST":
      form=careerstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         worldcuppoints=form.cleaned_data["worldcuppoints"]
         totalpoints=form.cleaned_data["totalpoints"]
         defaults={"worldcuppoints":worldcuppoints,"totalpoints":totalpoints}
         obj,created=pool_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"pool_app/submit_careerstats.html")
      else:
         print("error form invalid")      
    return render(request,"pool_app/form_careerstats.html",{"form":form}) 
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=pool_db.objects.get(name__iexact=name) 
         except pool_db.DoesNotExist:
             return render(request,"pool_app/error_player.html")
         return render(request,"pool_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"pool_app/search_player.html",{"form":form})
def search_about(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=pool_db.objects.get(name__iexact=name) 
         except pool_db.DoesNotExist:
             return render(request,"pool_app/error_about.html")
         return render(request,"pool_app/result_about.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"pool_app/search_about.html",{"form":form})
def search_details(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=pool_db.objects.get(name__iexact=name) 
         except pool_db.DoesNotExist:
             return render(request,"pool_app/error_details.html")
         return render(request,"pool_app/result_details.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"pool_app/search_details.html",{"form":form})
def search_pointstats(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=pool_db.objects.get(name__iexact=name) 
         except pool_db.DoesNotExist:
             return render(request,"pool_app/error_pointstats.html")
         return render(request,"pool_app/result_pointstats.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"pool_app/search_pointstats.html",{"form":form})
def search_careerstats(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=pool_db.objects.get(name__iexact=name) 
         except pool_db.DoesNotExist:
             return render(request,"pool_app/error_careerstats.html")
         return render(request,"pool_app/result_careerstats.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"pool_app/search_careerstats.html",{"form":form})

  
                                                                                                                                                                                                                 		    	    		    		    