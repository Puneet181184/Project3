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
from django.shortcuts import get_object_or_404
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
         return home(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/form.html",{"form":form}) 

def form_track(request):
    form=trackform()
    if request.method=="POST":
      form=trackform(request.POST)
      if form.is_valid():
         title=form.cleaned_data["title"]
         album=form.cleaned_data["album"]
         defaults={"album":album}
         obj,created=music_db.objects.update_or_create(title=title,defaults=defaults)
         return home(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/form_track.html",{"form":form})   

def form_artist(request):
    form=artistform()
    if request.method=="POST":
      form=artistform(request.POST)
      if form.is_valid():
         title=form.cleaned_data["title"]
         artist=form.cleaned_data["artist"]
         writer=form.cleaned_data["writer"]
         othername=form.cleaned_data["othername"]
         defaults={"artist":artist,"writer":writer,"othername":othername}
         obj,created=music_db.objects.update_or_create(title=title,defaults=defaults)
         return home(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/form_artist.html",{"form":form})   

def form_codes(request):
    form=codesform()
    if request.method=="POST":
      form=codesform(request.POST)
      if form.is_valid():
         title=form.cleaned_data["title"]
         isni=form.cleaned_data["isni"]
         ipi=form.cleaned_data["ipi"]
         isrc=form.cleaned_data["isrc"]
         defaults={"isni":isni,"ipi":ipi,"isrc":isrc}
         obj,created=music_db.objects.update_or_create(title=title,defaults=defaults)
         return home(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/form_codes.html",{"form":form})

def form_sesac(request):
    form=sesacform()
    if request.method=="POST":
      form=sesacform(request.POST)
      if form.is_valid():
         title=form.cleaned_data["title"]
         sesac_id=form.cleaned_data["sesac_id"]
         sesac_pub=form.cleaned_data["sesac_pub"]
         defaults={"sesac_id":sesac_id,"sesac_pub":sesac_pub}
         obj,created=music_db.objects.update_or_create(title=title,defaults=defaults)        
         return home(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/form_sesac.html",{"form":form})

def form_ascap(request):
    form=ascapform()
    if request.method=="POST":
      form=ascapform(request.POST)
      if form.is_valid():
         title=form.cleaned_data["title"]
         ascap_id=form.cleaned_data["ascap_id"]
         ascap_pub=form.cleaned_data["ascap_pub"]
         ascap_ipi=form.cleaned_data["ascap_ipi"]
         defaults={"ascap_id":ascap_id,"ascap_pub":ascap_pub,"ascap_ipi":ascap_ipi}
         obj,created=music_db.objects.update_or_create(title=title,defaults=defaults) 
         return home(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/form_ascap.html",{"form":form})

def form_bmi(request):
    form=bmiform()
    if request.method=="POST":
      form=bmiform(request.POST)
      if form.is_valid():
         title=form.cleaned_data["title"]
         bmi_id=form.cleaned_data["bmi_id"]
         bmi_pub=form.cleaned_data["bmi_pub"]
         defaults={"bmi_id":bmi_id,"bmi_pub":bmi_pub}
         obj,created=music_db.objects.update_or_create(title=title,defaults=defaults)
         return home(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/form_bmi.html",{"form":form})

def form_gmr(request):
    form=gmrform()
    if request.method=="POST":
      form=gmrform(request.POST)
      if form.is_valid():
         title=form.cleaned_data["title"]
         gmr_id=form.cleaned_data["gmr_id"]
         gmr_pub=form.cleaned_data["gmr_pub"]
         gmr_ipi=form.cleaned_data["gmr_ipi"]
         defaults={"gmr_id":gmr_id,"gmr_pub":gmr_pub,"gmr_ipi":gmr_ipi}
         obj,created=music_db.objects.update_or_create(title=title,defaults=defaults) 
         return home(request)
      else:
         print("error form invalid")      
    return render(request,"music_app/form_gmr.html",{"form":form})

def search_track(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST)
      if form.is_valid():
         title=form.cleaned_data["title"]
         my_value=get_object_or_404(music_db,title=title)
         return render(request,"music_app/result_track.html",context={"music":my_value})
      else:
         print("error form invalid")      
    return render(request,"music_app/search_track.html",{"form":form})

def search_artist(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST)
      if form.is_valid():
         title=form.cleaned_data["title"]
         my_value=get_object_or_404(music_db,title=title)
         return render(request,"music_app/result_artist.html",context={"music":my_value})
      else:
         print("error form invalid")      
    return render(request,"music_app/search_artist.html",{"form":form})


def search_ascap(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST)
      if form.is_valid():
         title=form.cleaned_data["title"]
         my_value=get_object_or_404(music_db,title=title)
         return render(request,"music_app/result_ascap.html",context={"music":my_value})
      else:
         print("error form invalid")      
    return render(request,"music_app/search_ascap.html",{"form":form})

def search_bmi(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST)
      if form.is_valid():
         title=form.cleaned_data["title"]
         my_value=get_object_or_404(music_db,title=title)
         return render(request,"music_app/result_bmi.html",context={"music":my_value})
      else:
         print("error form invalid")      
    return render(request,"music_app/search_bmi.html",{"form":form})

def search_codes(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST)
      if form.is_valid():
         title=form.cleaned_data["title"]
         my_value=get_object_or_404(music_db,title=title)
         return render(request,"music_app/result_codes.html",context={"music":my_value})
      else:
         print("error form invalid")      
    return render(request,"music_app/search_codes.html",{"form":form})


def search_gmr(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST)
      if form.is_valid():
         title=form.cleaned_data["title"]
         my_value=get_object_or_404(music_db,title=title)
         return render(request,"music_app/result_gmr.html",context={"music":my_value})
      else:
         print("error form invalid")      
    return render(request,"music_app/search_gmr.html",{"form":form})


def search_sesac(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST)
      if form.is_valid():
         title=form.cleaned_data["title"]
         my_value=get_object_or_404(music_db,title=title)
         return render(request,"music_app/result_sesac.html",context={"music":my_value})
      else:
         print("error form invalid")      
    return render(request,"music_app/search_sesac.html",{"form":form})

























