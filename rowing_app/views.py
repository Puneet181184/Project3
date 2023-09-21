from django.shortcuts import render
from rowing_app.models import rowing_db
from rowing_app.forms import playerform
from rowing_app.forms import aboutform
from rowing_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"rowing_app/home.html")
def player(request):
    players_list=rowing_db.objects.order_by("name")
    rowing_dict={"player":players_list}
    return render(request,"rowing_app/player.html",context=rowing_dict)		
def about(request):
    players_list=rowing_db.objects.order_by("name")
    rowing_dict={"player":players_list}
    return render(request,"rowing_app/about.html",context=rowing_dict)     
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         country=form.cleaned_data["country"]
         defaults={"age":age,"country":country}
         obj,created=rowing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"rowing_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"rowing_app/form_player.html",{"form":form}) 
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         height=form.cleaned_data["height"]
         weight=form.cleaned_data["weight"]
         defaults={"height":height,"weight":weight}
         obj,created=rowing_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"rowing_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"rowing_app/form_about.html",{"form":form})          
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=rowing_db.objects.get(name__iexact=name) 
         except rowing_db.DoesNotExist:
             return render(request,"rowing_app/error_player.html")
         return render(request,"rowing_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"rowing_app/search_player.html",{"form":form})
def search_about(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=rowing_db.objects.get(name__iexact=name) 
         except rowing_db.DoesNotExist:
             return render(request,"rowing_app/error_about.html")
         return render(request,"rowing_app/result_about.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"rowing_app/search_about.html",{"form":form})      
