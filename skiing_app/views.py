from django.shortcuts import render
from skiing_app.models import skiing_db
from skiing_app.forms import playerform
from skiing_app.forms import aboutform
from skiing_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"skiing_app/home.html")
def player(request):
    players_list=skiing_db.objects.order_by("name")
    skiing_dict={"player":players_list}
    return render(request,"skiing_app/player.html",context=skiing_dict)		
def about(request):
    players_list=skiing_db.objects.order_by("name")
    skiing_dict={"player":players_list}
    return render(request,"skiing_app/about.html",context=skiing_dict)     
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         dob=form.cleaned_data["dob"]
         defaults={"age":age,"dob":dob}
         obj,created=skiing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"skiing_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"skiing_app/form_player.html",{"form":form})    
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         height=form.cleaned_data["height"]
         skitype=form.cleaned_data["skitype"]
         defaults={"height":height,"skitype":skitype}
         obj,created=skiing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"skiing_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"skiing_app/form_about.html",{"form":form}) 
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=skiing_db.objects.get(name__iexact=name) 
         except skiing_db.DoesNotExist:
             return render(request,"skiing_app/error_player.html")
         return render(request,"skiing_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"skiing_app/search_player.html",{"form":form}) 
def search_about(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=skiing_db.objects.get(name__iexact=name) 
         except skiing_db.DoesNotExist:
             return render(request,"skiing_app/error_about.html")
         return render(request,"skiing_app/result_about.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"skiing_app/search_about.html",{"form":form})                    