from django.shortcuts import render

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"archery_app/home.html")
