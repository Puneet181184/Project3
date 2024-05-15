from django.shortcuts import render
from skiing_app.models import skiing_db
from skiing_app.forms import playerform
from skiing_app.forms import aboutform
from skiing_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"skiing_app/home.html")
