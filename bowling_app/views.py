from django.shortcuts import render

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"bowling_app/home.html")
