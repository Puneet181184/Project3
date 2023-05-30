from django.shortcuts import render
from iceskating_app.models import iceskating_db
from iceskating_app.forms import playerform
from iceskating_app.forms import aboutform
from iceskating_app.forms import detailsform
from iceskating_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"iceskating_app/home.html")
def player(request):
    players_list=iceskating_db.objects.order_by("name")
    iceskating_dict={"player":players_list}
    return render(request,"iceskating_app/player.html",context=iceskating_dict)			
def about(request):
    players_list=iceskating_db.objects.order_by("name")
    iceskating_dict={"player":players_list}
    return render(request,"iceskating_app/about.html",context=iceskating_dict)			
def details(request):
    players_list=iceskating_db.objects.order_by("name")
    iceskating_dict={"player":players_list}
    return render(request,"iceskating_app/details.html",context=iceskating_dict)			
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         country=form.cleaned_data["country"]
         defaults={"age":age,"country":country}
         obj,created=iceskating_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"iceskating_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"iceskating_app/form_player.html",{"form":form})       