from django.shortcuts import render
from rowing_app.models import rowing_db
from rowing_app.forms import playerform
from rowing_app.forms import aboutform
from rowing_app.forms import detailsform
from rowing_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"rowing_app/home.html")