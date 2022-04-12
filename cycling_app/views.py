from django.shortcuts import render

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"cycling_app/home.html")
