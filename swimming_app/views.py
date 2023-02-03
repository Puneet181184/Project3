from django.shortcuts import render
from swimming_app.models import swimming_db
from swimming_app.forms import playerform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"swimming_app/home.html")
def player(request):
    players_list=swimming_db.objects.order_by("name")
    swimming_dict={"player":players_list}
    return render(request,"swimming_app/player.html",context=swimming_dict)		
def about(request):
    players_list=swimming_db.objects.order_by("name")
    swimming_dict={"player":players_list}
    return render(request,"swimming_app/about.html",context=swimming_dict)
def details(request):
    players_list=swimming_db.objects.order_by("name")
    swimming_dict={"player":players_list}
    return render(request,"swimming_app/details.html",context=swimming_dict)
def pointstats(request):
    players_list=swimming_db.objects.order_by("name")
    swimming_dict={"player":players_list}
    return render(request,"swimming_app/pointstats.html",context=swimming_dict)		    		    		    
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         country=form.cleaned_data["country"]
         defaults={"age":age,"country":country}
         obj,created=swimming_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"swimming_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"swimming_app/form_player.html",{"form":form})         
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         rank=form.cleaned_data["rank"]
         defaults={"rank":rank}
         obj,created=swimming_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"swimming_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"swimming_app/form_about.html",{"form":form})   
def form_details(request):
    form=detailsform()
    if request.method=="POST":
      form=detailsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         medals=form.cleaned_data["medals"]
         defaults={"medals":medals}
         obj,created=swimming_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"swimming_app/submit_medals.html")
      else:
         print("error form invalid")      
    return render(request,"swimming_app/form_medals.html",{"form":form})   
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
         obj,created=swimming_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"swimming_app/submit_pointstats.html")
      else:
         print("error form invalid")      
    return render(request,"swimming_app/form_pointstats.html",{"form":form})                                 