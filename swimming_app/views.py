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