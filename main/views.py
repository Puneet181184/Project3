from django.shortcuts import render
# Create your views here.
def main(request):
	#return HttpResponse("Hello World!")
	return render(request,"home.html")	