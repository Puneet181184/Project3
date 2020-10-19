from django.shortcuts import render
from django.http import HttpResponse
from music_app.models import music_db
from music_app.forms import newuserform
from music_app.forms import trackform
from music_app.forms import artistform
from music_app.forms import codesform
from music_app.forms import sesacform
from music_app.forms import ascapform
from music_app.forms import bmiform
from music_app.forms import gmrform
from music_app.forms import searchform
# Create your views here.
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"music_app/home.html")
def track(request):
    music_list=music_db.objects.order_by("title")
    music_dict={"music":music_list}
    return render(request,"music_app/track.html",context=music_dict)
def artist(request):
    music_list=music_db.objects.order_by("title")
    music_dict={"music":music_list}
    return render(request,"music_app/artist.html",context=music_dict)
def codes(request):
    music_list=music_db.objects.order_by("title")
    music_dict={"music":music_list}
    return render(request,"music_app/codes.html",context=music_dict)
def sesac(request):
    music_list=music_db.objects.order_by("title")
    music_dict={"music":music_list}
    return render(request,"music_app/sesac.html",context=music_dict)
def ascap(request):
    music_list=music_db.objects.order_by("title")
    music_dict={"music":music_list}
    return render(request,"music_app/ascap.html",context=music_dict) 
def bmi(request):
    music_list=music_db.objects.order_by("title")
    music_dict={"music":music_list}
    return render(request,"music_app/bmi.html",context=music_dict)    
def gmr(request):
    music_list=music_db.objects.order_by("title")
    music_dict={"music":music_list}
    return render(request,"music_app/gmr.html",context=music_dict)
def form_music(request):
    form=newuserform()
    if request.method=="POST":
      form=newuserform(request.POST)
      if form.is_valid():
         form.save(commit=True)
         return index(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/form.html",{"form":form}) 

def form_track(request):
    form=trackform()
    if request.method=="POST":
      form=trackform(request.POST)
      if form.is_valid():
         form.save(commit=True)
         return index(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/form_track.html",{"form":form})   

def form_artist(request):
    form=artistform()
    if request.method=="POST":
      form=artistform(request.POST)
      if form.is_valid():
         form.save(commit=True)
         return index(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/form_artist.html",{"form":form})   

def form_codes(request):
    form=codesform()
    if request.method=="POST":
      form=codesform(request.POST)
      if form.is_valid():
         form.save(commit=True)
         return index(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/form_codes.html",{"form":form})

def form_sesac(request):
    form=sesacform()
    if request.method=="POST":
      form=sesacform(request.POST)
      if form.is_valid():
         form.save(commit=True)
         return index(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/form_sesac.html",{"form":form})

def form_ascap(request):
    form=ascapform()
    if request.method=="POST":
      form=ascapform(request.POST)
      if form.is_valid():
         form.save(commit=True)
         return index(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/form_ascap.html",{"form":form})

def form_bmi(request):
    form=bmiform()
    if request.method=="POST":
      form=bmiform(request.POST)
      if form.is_valid():
         form.save(commit=True)
         return index(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/form_bmi.html",{"form":form})

def form_gmr(request):
    form=gmrform()
    if request.method=="POST":
      form=gmrform(request.POST)
      if form.is_valid():
         form.save(commit=True)
         return index(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/form_gmr.html",{"form":form})

def search_track(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST)
      if form.is_valid():
         #form.save(commit=True)
         return index(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/search_track.html",{"form":form})

def search_artist(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST)
      if form.is_valid():
         #form.save(commit=True)
         return index(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/search_artist.html",{"form":form})


def search_ascap(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST)
      if form.is_valid():
         #form.save(commit=True)
         return index(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/search_ascap.html",{"form":form})

def search_bmi(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST)
      if form.is_valid():
         #form.save(commit=True)
         return index(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/search_bmi.html",{"form":form})

def search_codes(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST)
      if form.is_valid():
         #form.save(commit=True)
         return index(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/search_codes.html",{"form":form})


def search_gmr(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST)
      if form.is_valid():
         #form.save(commit=True)
         return index(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/search_gmr.html",{"form":form})


def search_sesac(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST)
      if form.is_valid():
         #form.save(commit=True)
         return index(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/search_sesac.html",{"form":form})

























