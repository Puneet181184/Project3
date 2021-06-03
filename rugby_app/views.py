from django.shortcuts import render
from rugby_app.models import rugby_db
from rugby_app.forms import playerform
# Create your views here.
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"rugby_app/home.html")
def player(request):
    players_list=rugby_db.objects.order_by("name")
    rugby_dict={"player":players_list}
    return render(request,"rugby_app/player.html",context=rugby_dict)			
def about(request):
    players_list=rugby_db.objects.order_by("name")
    rugby_dict={"player":players_list}
    return render(request,"rugby_app/about.html",context=rugby_dict)		
def details(request):
    players_list=rugby_db.objects.order_by("name")
    rugby_dict={"player":players_list}
    return render(request,"rugby_app/details.html",context=rugby_dict)
def matchstats(request):
    players_list=rugby_db.objects.order_by("name")
    rugby_dict={"player":players_list}
    return render(request,"rugby_app/matchstats.html",context=rugby_dict)
def gamestats(request):
    players_list=rugby_db.objects.order_by("name")
    rugby_dict={"player":players_list}
    return render(request,"rugby_app/gamestats.html",context=rugby_dict)
def pointstats(request):
    players_list=rugby_db.objects.order_by("name")
    rugby_dict={"player":players_list}
    return render(request,"rugby_app/pointstats.html",context=rugby_dict)
def cardstats(request):
    players_list=rugby_db.objects.order_by("name")
    rugby_dict={"player":players_list}
    return render(request,"rugby_app/cardstats.html",context=rugby_dict)

def form_player(request):
    form=playerform()
    if request.method=="POST":
      form=playerform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         age=form.cleaned_data["age"]
         dob=form.cleaned_data["dob"]
         nationality=form.cleaned_data["nationality"]
         defaults={"age":age,"dob":dob,"nationality":nationality}
         obj,created=rugby_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"rugby_app/submit_player.html")
      else:
         print("error form invalid")      
    return render(request,"rugby_app/form_player.html",{"form":form})
def form_about(request):
    form=aboutform()
    if request.method=="POST":
      form=aboutform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         team=form.cleaned_data["team"]
         position=form.cleaned_data["position"]
         defaults={"team":team,"position"position}
         obj,created=rugby_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"rugby_app/submit_about.html")
      else:
         print("error form invalid")      
    return render(request,"rugby_app/form_about.html",{"form":form})
def form_details(request):    
    form=detailsform()
    if request.method=="POST":
      form=detailsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         debut=form.cleaned_data["debut"]
         height=form.cleaned_data["height"]
         weight=form.cleaned_data["weight"]
         defaults={"debut":debut,"height":height,"weight":weight}
         obj,created=rugby_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"rugby_app/submit_details.html")
      else:
         print("error form invalid")  
    return render(request,"rugby_app/form_details.html",{"form":form}) 
def form_matchstats(request):    
    form=matchstatsform()
    if request.method=="POST":
      form=matchstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         matches=form.cleaned_data["matches"]
         wins=form.cleaned_data["wins"]
         draws=form.cleaned_data["drwas"]
         losses=form.cleaned_data["losses"]
         defaults={"matches":matches,"wins":wins,"draws":draws,"losses":losses}
         obj,created=rugby_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"rugby_app/submit_matchstats.html")
      else:
         print("error form invalid")  
    return render(request,"rugby_app/form_matchstats.html",{"form":form})
def form_gamestats(request):    
    form=gamestatsform()
    if request.method=="POST":
      form=gamestatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         minutes=form.cleaned_data["minutes"]
         started=form.cleaned_data["started"]
         defaults={"minutes":minutes,"started":started}
         obj,created=rugby_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"rugby_app/submit_gamestats.html")
      else:
         print("error form invalid")  
    return render(request,"rugby_app/form_gamestats.html",{"form":form})
def form_pointstats(request):    
    form=pointstatsform()
    if request.method=="POST":
      form=pointstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         points=form.cleaned_data["points"]
         tries=form.cleaned_data["tries"]
         drops=form.cleaned_data["drops"]
         penalties=form.cleaned_data["penalties"]
         conversions=form.cleaned_data["conversions"]
         defaults={"points":points,"tries":tries,"drops":drops,"penalties":penalties,"conversions":conversions}
         obj,created=rugby_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"rugby_app/submit_pointstats.html")
      else:
         print("error form invalid")  
    return render(request,"rugby_app/form_pointstats.html",{"form":form}) 
def form_cardstats(request):    
    form=cardstatsform()
    if request.method=="POST":
      form=cardstatsform(request.POST)
      if form.is_valid():
         name=form.cleaned_data["name"]
         yellowcards=form.cleaned_data["yellowcards"]
         redcards=form.cleaned_data["redcards"]
         defaults={"yellowcards":yellowcards,"redcards":redcards}
         obj,created=rugby_db.objects.update_or_create(name=name,defaults=defaults)
         return render(request,"rugby_app/submit_cardstats.html")
      else:
         print("error form invalid")  
    return render(request,"rugby_app/form_cardstats.html",{"form":form}) 






























































    


       	    	    	    	    	          	    	        	    	    	    	    	          	    	    	    	    	          	    	    	    	    	           	    	    	    	    	