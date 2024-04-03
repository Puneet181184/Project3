from django.shortcuts import render
from boxing_app.models import boxing_db
from boxing_app.forms import playerform
from boxing_app.forms import aboutform
from boxing_app.forms import detailsform
from boxing_app.forms import gamestatsform
from boxing_app.forms import pointstatsform
from boxing_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"boxing_app/home.html")
