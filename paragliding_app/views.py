from django.shortcuts import render
from paragliding_app.models import paragliding_db
from paragliding_app.forms import playerform
from paragliding_app.forms import aboutform
from paragliding_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"paragliding_app/home.html")
def player(request):
    players_list=paragliding_db.objects.order_by("name")
    paragliding_dict={"player":players_list}
    return render(request,"paragliding_app/player.html",context=paragliding_dict)		
def about(request):
    players_list=paragliding_db.objects.order_by("name")
    paragliding_dict={"player":players_list}
    return render(request,"paragliding_app/about.html",context=paragliding_dict)
def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         country=form.cleaned_data["country"]
         defaults={"age":age,"country":country}
         obj,created=paragliding_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"paragliding_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"paragliding_app/form_player.html",{"form":form})                                      
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         Id=form.cleaned_data["Id"]
         gender=form.cleaned_data["Gender"]
         defaults={"id":Id,"gender":gender}
         obj,created=_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"paragliding_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"paragliding_app/form_about.html",{"form":form}) 
def search_player(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=paragliding_db.objects.get(name__iexact=name) 
         except kickboxing_db.DoesNotExist:
             return render(request,"paragliding_app/error_player.html")
         return render(request,"paragliding_app/result_player.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"paragliding_app/search_player.html",{"form":form})
def search_about(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         name=form.cleaned_data["name"]
         try:
             my_value=paragliding_db.objects.get(name__iexact=name) 
         except kickboxing_db.DoesNotExist:
             return render(request,"paragliding_app/error_about.html")
         return render(request,"paragliding_app/result_about.html",context={"player":my_value})
      else:
         print(" error form invalid")
    return render(request,"paragliding_app/search_about.html",{"form":form})           