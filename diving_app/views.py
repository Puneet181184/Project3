from django.shortcuts import render
from diving_app.models import diving_db
from diving_app.forms import playerform
from diving_app.forms import aboutform
from diving_app.forms import searchform
# Create your views here.
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"diving_app/home.html")
def player(request):
    players_list=diving_db.objects.order_by("name")
    diving_dict={"player":players_list}
    return render(request,"diving_app/player.html",context=diving_dict)		
def about(request):
    players_list=diving_db.objects.order_by("name")
    diving_dict={"player":players_list}
    return render(request,"diving_app/about.html",context=diving_dict)	
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         dob=form.cleaned_data["dob"]
         country=form.cleaned_data["country"]
         defaults={"dob":dob,"country":country}
         obj,created=diving_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"diving_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"diving_app/form_player.html",{"form":form})         
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         gender=form.cleaned_data["gender"]
         discipline=form.cleaned_data["discipline"]
         defaults={"gender":gender,"discipline":discipline}
         obj,created=diving_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"diving_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"diving_app/form_about.html",{"form":form})             