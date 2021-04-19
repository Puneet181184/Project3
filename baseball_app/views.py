from django.shortcuts import render



def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"baseball_app/home.html")


