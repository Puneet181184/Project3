from django.shortcuts import render

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"karate_app/home.html")
