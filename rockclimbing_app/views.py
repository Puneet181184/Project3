from django.shortcuts import render
from rockclimbing_app.models import rockclimbing_db
from rockclimbing_app.forms import playerform
from rockclimbing_app.forms import aboutform
from rockclimbing_app.forms import pointstatsform
from rockclimbing_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"rockclimbing_app/home.html")
def player(request):
    players_list=rockclimbing_db.objects.order_by("name")
    rockclimbing_dict={"player":players_list}
    return render(request,"rockclimbing_app/player.html",context=rockclimbing_dict)
def about(request):
    players_list=rockclimbing_db.objects.order_by("name")
    rockclimbing_dict={"player":players_list}
    return render(request,"rockclimbing_app/about.html",context=rockclimbing_dict)       
def pointstats(request):
    players_list=rockclimbing_db.objects.order_by("name")
    rockclimbing_dict={"player":players_list}
    return render(request,"rockclimbing_app/pointstats.html",context=rockclimbing_dict)    
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         country=form.cleaned_data["country"]
         defaults={"age":age,"country":country}
         obj,created=rockclimbing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"rockclimbing_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"rockclimbing_app/form_player.html",{"form":form})        
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         height=form.cleaned_data["height"]
         weight=form.cleaned_data["weight"]
         defaults={"height":height,"weight":weight}
         obj,created=kickboxing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"kickboxing_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"kickboxing_app/form_about.html",{"form":form})
def form_pointstats(request):
    form=pointstatsform()
    if request.method=="POST":
      form=pointstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         rankingboulder=form.cleaned_data["rankingboulder"]
         rankinglead=form.cleaned_data["rankinglead"]
         defaults={"rankingboulder":rankingboulder,"rankinglead":rankinglead}
         obj,created=kickboxing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"kickboxing_app/submit_pointstats.html")
      else:
         print("error form invalid")      
    return render(request,"kickboxing_app/form_pointstats.html",{"form":form})                