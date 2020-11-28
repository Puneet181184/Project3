from django.shortcuts import render

# Create your views here.
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"cricket_app/home.html")

