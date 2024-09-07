from django.shortcuts import render
from hockey_app.models import hockey_db
from hockey_app.forms import playerform
from hockey_app.forms import aboutform
from hockey_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"hockey_app/home.html")
