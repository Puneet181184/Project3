from django.shortcuts import render
from iceskating_app.models import iceskating_db
from iceskating_app.forms import playerform
from archery_app.forms import aboutform
from archery_app.forms import detailsform
from archery_app.forms import gamestatsform
from archery_app.forms import pointstatsform
from archery_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"iceskating_app/home.html")
