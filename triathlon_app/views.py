from django.shortcuts import render
from triathlon_app.models import triathlon_db
from triathlon_app.forms import playerform
from triathlon_app.forms import aboutform
from triathlon_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"triathlon_app/home.html")
