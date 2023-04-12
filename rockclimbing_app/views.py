from django.shortcuts import render
from rockclimbing_app.models import rockclimbing_db
from archery_app.forms import playerform
from archery_app.forms import aboutform
from archery_app.forms import detailsform
from archery_app.forms import gamestatsform
from archery_app.forms import pointstatsform
from archery_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"rockclimbing_app/home.html")
