from django.shortcuts import render
from paragliding_app.models import paragliding_db
from paragliding_app.forms import playerform
from paragliding_app.forms import aboutform
from paragliding_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"paragliding_app/home.html")
