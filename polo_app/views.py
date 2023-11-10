from django.shortcuts import render
from polo_app.models import polo_db
from polo_app.forms import playerform
from polo_app.forms import aboutform
from polo_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"polo_app/home.html")
def player(request):
    players_list=polo_db.objects.order_by("name")
    polo_dict={"player":players_list}
    return render(request,"polo_app/player.html",context=polo_dict)	
def about(request):
    players_list=polo_db.objects.order_by("name")
    polo_dict={"player":players_list}
    return render(request,"polo_app/about.html",context=polo_dict)
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         country=form.cleaned_data["country"]
         defaults={"age":age,"country":country}
         obj,created=polo_db.objects.update_or_create(title=title,defaults=defaults)
         return render(request,"polo_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"polo_app/form_player.html",{"form":form})            
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         status=form.cleaned_data["status"]
         points=form.cleaned_data["points"]
         defaults={"status":status,"points":points}
         obj,created=polo_db.objects.update_or_create(title=title,defaults=defaults)
         return render(request,"polo_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"polo_app/form_about.html",{"form":form})                
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=polo_db.objects.get(name__iexact=name) 
         except polo_db.DoesNotExist:
             return render(request,"polo_app/error_player.html")
         return render(request,"polo_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"polo_app/search_player.html",{"form":form})  
def search_about(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=polo_db.objects.get(name__iexact=name) 
         except polo_db.DoesNotExist:
             return render(request,"polo_app/error_about.html")
         return render(request,"polo_app/result_about.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"polo_app/search_about.html",{"form":form})      

