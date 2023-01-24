from django.shortcuts import render
from swimming_app.models import swimming_db

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"swimming_app/home.html")
