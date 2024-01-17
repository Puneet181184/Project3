from django.shortcuts import render
from handball_app.models import handball_db
from handball_app.forms import playerform
from handball_app.forms import aboutform
from handball_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"handball_app/home.html")
