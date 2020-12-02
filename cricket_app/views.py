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
