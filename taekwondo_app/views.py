from django.shortcuts import render
from taekwondo_app.models import taekwondo_db
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"taekwondo_app/home.html")
def player(request):
    players_list=taekwondo_db.objects.order_by("name")
    taekwondo_dict={"player":players_list}
    return render(request,"taekwondo_app/player.html",context=taekwondo_dict)	
def about(request):
    players_list=taekwondo_db.objects.order_by("name")
    taekwondo_dict={"player":players_list}
    return render(request,"taekwondo_app/about.html",context=taekwondo_dict)	    
def details(request):
    players_list=taekwondo_db.objects.order_by("name")
    taekwondo_dict={"player":players_list}
    return render(request,"taekwondo_app/details.html",context=taekwondo_dict)	
def pointstats(request):
    players_list=taekwondo_db.objects.order_by("name")
    taekwondo_dict={"player":players_list}
    return render(request,"taekwondo_app/pointstats.html",context=taekwondo_dict)	
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
         obj,created=taekwondo_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"taekwondo_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"taekwondo_app/form_player.html",{"form":form})                 
