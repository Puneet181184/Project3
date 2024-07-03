from django.shortcuts import render
from skating_app.models import skating_db
from skating_app.forms import playerform
from skating_app.forms import aboutform
from skating_app.forms import searchform

# Create your views here.
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"skating_app/home.html")
def player(request):
    players_list=skating_db.objects.order_by("name")
    skating_dict={"player":players_list}
    return render(request,"skating_app/player.html",context=skating_dict)			
def about(request):
    players_list=skating_db.objects.order_by("name")
    skating_dict={"player":players_list}
    return render(request,"skating_app/about.html",context=skating_dict)	
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         dob=form.cleaned_data["dob"]
         defaults={"age":age,"dob":dob}
         obj,created=skating_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"skating_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"skating_app/form_player.html",{"form":form})
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         gender=form.cleaned_data["gender"]
         club=form.cleaned_data["club"]
         defaults={"gender":gender,"club":club}
         obj,created=skating_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"skating_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"skating_app/form_about.html",{"form":form})    