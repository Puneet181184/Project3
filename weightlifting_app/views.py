from django.shortcuts import render
from weightlifting_app.models import weightlifting_db
from weightlifting_app.forms import playerform
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"weightlifting_app/home.html")
def player(request):
    players_list=weightlifting_db.objects.order_by("name")
    weightlifting_dict={"player":players_list}
    return render(request,"weightlifting_app/player.html",context=weightlifting_dict)		
def about(request):
    players_list=weightlifting_db.objects.order_by("name")
    weightlifting_dict={"player":players_list}
    return render(request,"weightlifting_app/about.html",context=weightlifting_dict)       
def details(request):
    players_list=weightlifting_db.objects.order_by("name")
    weightlifting_dict={"player":players_list}
    return render(request,"weightlifting_app/details.html",context=weightlifting_dict)       
def careerstats(request):
    players_list=weightlifting_db.objects.order_by("name")
    weightlifting_dict={"player":players_list}
    return render(request,"weightlifting_app/careerstats.html",context=weightlifting_dict)       
def matchstats(request):
    players_list=weightlifting_db.objects.order_by("name")
    weightlifting_dict={"player":players_list}
    return render(request,"weightlifting_app/matchstats.html",context=weightlifting_dict)       
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
         obj,created=weightlifting_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"weightlifting_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"weightlifting_app/form_player.html",{"form":form})     