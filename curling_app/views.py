from django.shortcuts import render
from curling_app.models import curling_db
from curling_app.forms import playerform
from curling_app.forms import aboutform
from curling_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"curling_app/home.html")
def player(request):
    players_list=curling_db.objects.order_by("name")
    curling_dict={"player":players_list}
    return render(request,"curling_app/player.html",context=curling_dict)
def about(request):
    players_list=curling_db.objects.order_by("name")
    curling_dict={"player":players_list}
    return render(request,"curling_app/about.html",context=curling_dict)    
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         country=form.cleaned_data["country"]
         defaults={"age":age,"country":country}
         obj,created=curling_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"curling_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"curling_app/form_player.html",{"form":form})        
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         ranking=form.cleaned_data["ranking"]
         defaults={"ranking":ranking}
         obj,created=curling_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"curling_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"curling_app/form_about.html",{"form":form})        