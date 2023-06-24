from django.shortcuts import render
from curling_app.models import curling_db
from curling_app.forms import playerform
from curling_app.forms import aboutform
from curling_app.forms import detailsform
from curling_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"curling_app/home.html")
