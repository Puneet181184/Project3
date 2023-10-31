from django.shortcuts import render
from polo_app.models import polo_db
from polo_app.forms import playerform
from polo_app.forms import aboutform
from polo_app.forms import detailsform
from archery_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"polo_app/home.html")
