from django.shortcuts import render
from books_app.models import books_db
from books_app.forms import bookform

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

def form_book(request):
    form=bookform()
    if request.method=="POST":
      form=bookform(request.POST)
      if form.is_valid():
         title=form.cleaned_data["title"]
         pages=form.cleaned_data["pages"]
         defaults={"pages":pages}
         obj,created=books_db.objects.update_or_create(title=title,defaults=defaults)
         return render(request,"books_app/submit_book.html")
      else:
         print("error form invalid")      
    return render(request,"books_app/form_book.html",{"form":form})   
