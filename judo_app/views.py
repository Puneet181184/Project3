from django.shortcuts import render
from judo_app.models import judo_db
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"judo_app/home.html")
