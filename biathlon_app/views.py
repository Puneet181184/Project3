from django.shortcuts import render
from biathlon_app.models import biathlon_db
from biathlon_app.forms import playerform
from biathlon_app.forms import aboutform
from biathlon_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"biathlon_app/home.html")
