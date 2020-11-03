from django.shortcuts import render
from books_app.models import books_db

# Create your views here.
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"books_app/home.html")

def book(request):
    books_list=books_db.objects.order_by("title")
    books_dict={"book":books_list}
    return render(request,"books_app/book.html",context=books_dict)	

def author(request):
    books_list=books_db.objects.order_by("title")
    books_dict={"book":books_list}
    return render(request,"books_app/author.html",context=books_dict)	    

def codes(request):
    books_list=books_db.objects.order_by("title")
    books_dict={"book":books_list}
    return render(request,"books_app/codes.html",context=books_dict)	    

def other(request):
    books_list=books_db.objects.order_by("title")
    books_dict={"book":books_list}
    return render(request,"books_app/other.html",context=books_dict)	        