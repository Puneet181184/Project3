from django.shortcuts import render
from horseracing_app.models import horseracing_db
from horseracing_app.forms import playerform
from horseracing_app.forms import aboutform
from horseracing_app.forms import detailsform
from horseracing_app.forms import pointstatsform
from horseracing_app.forms import searchform


def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"horseracing_app/home.html")
def player(request):
    players_list=horseracing_db.objects.order_by("name")
    horseracing_dict={"player":players_list}
    return render(request,"horseracing_app/player.html",context=horseracing_dict)		
def about(request):
    players_list=horseracing_db.objects.order_by("name")
    horseracing_dict={"player":players_list}
    return render(request,"horseracing_app/about.html",context=horseracing_dict)
def details(request):
    players_list=horseracing_db.objects.order_by("name")
    horseracing_dict={"player":players_list}
    return render(request,"horseracing_app/details.html",context=horseracing_dict)		    		    
def pointstats(request):
    players_list=horseracing_db.objects.order_by("name")
    horseracing_dict={"player":players_list}
    return render(request,"horseracing_app/pointstats.html",context=horseracing_dict)
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         defaults={"age":age}
         obj,created=horseracing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"horseracing_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"horseracing_app/form_player.html",{"form":form}) 
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         rank=form.cleaned_data["rank"]
         defaults={"rank":rank}
         obj,created=horseracing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"horseracing_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"horseracing_app/form_about.html",{"form":form}) 
def form_details(request):
    form=detailsform()
    if request.method=="POST":
      form=detailsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         horse=form.cleaned_data["horse"]
         starts=form.cleaned_data["starts"]
         defaults={"horse":horse,"starts":starts}
         obj,created=horseracing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"horseracing_app/submit_details.html")
      else:
         print("error form invalid")      
    return render(request,"horseracing_app/form_details.html",{"form":form}) 
def form_pointstats(request):
    form=pointstatsform()
    if request.method=="POST":
      form=pointstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         gold=form.cleaned_data["gold"]
         silver=form.cleaned_data["silver"]
         bronze=form.cleaned_data["bronze"]
         defaults={"gold":gold,"silver":silver,"bronze":bronze}
         obj,created=horseracing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"horseracing_app/submit_pointstats.html")
      else:
         print("error form invalid")      
    return render(request,"horseracing_app/form_pointstats.html",{"form":form})  
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=horseracing_db.objects.get(name__iexact=name) 
         except archery_db.DoesNotExist:
             return render(request,"horseracing_app/error_player.html")
         return render(request,"horseracing_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"horseracing_app/search_player.html",{"form":form}) 
def search_about(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=horseracing_db.objects.get(name__iexact=name) 
         except archery_db.DoesNotExist:
             return render(request,"horseracing_app/error_about.html")
         return render(request,"horseracing_app/result_about.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"horseracing_app/search_about.html",{"form":form}) 
def search_details(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=horseracing_db.objects.get(name__iexact=name) 
         except archery_db.DoesNotExist:
             return render(request,"horseracing_app/error_details.html")
         return render(request,"horseracing_app/result_details.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"horseracing_app/search_details.html",{"form":form})    
def search_pointstats(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=horseracing_db.objects.get(name__iexact=name) 
         except archery_db.DoesNotExist:
             return render(request,"horseracing_app/error_pointstats.html")
         return render(request,"horseracing_app/result_pointstats.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"horseracing_app/search_pointstats.html",{"form":form})      



