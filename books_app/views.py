from django.shortcuts import render
from books_app.models import books_db
from books_app.forms import bookform
from books_app.forms import authorform
from books_app.forms import codesform
from books_app.forms import otherform
from books_app.forms import searchform
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


def form_author(request):
    form=authorform()
    if request.method=="POST":
      form=authorform(request.POST)
      if form.is_valid():
         title=form.cleaned_data["title"]
         author=form.cleaned_data["author"]
         publisher=form.cleaned_data["publisher"]
         defaults={"author":author,"publisher":publisher}
         obj,created=books_db.objects.update_or_create(title=title,defaults=defaults)
         return render(request,"books_app/submit_author.html")
      else:
         print("error form invalid")      
    return render(request,"books_app/form_author.html",{"form":form})  

def form_codes(request):
    form=codesform()
    if request.method=="POST":
      form=codesform(request.POST)
      if form.is_valid():
         title=form.cleaned_data["title"]
         isbn=form.cleaned_data["isbn"]
         defaults={"isbn":isbn}
         obj,created=books_db.objects.update_or_create(title=title,defaults=defaults)
         return render(request,"books_app/submit_codes.html")
      else:
         print("error form invalid")      
    return render(request,"books_app/form_codes.html",{"form":form})  

def form_other(request):
    form=otherform()
    if request.method=="POST":
      form=otherform(request.POST)
      if form.is_valid():
         title=form.cleaned_data["title"]
         year=form.cleaned_data["year"]
         price=form.cleaned_data["price"]
         defaults={"year":year,"price":price}
         obj,created=books_db.objects.update_or_create(title=title,defaults=defaults)
         return render(request,"books_app/submit_other.html")
      else:
         print("error form invalid")      
    return render(request,"books_app/form_other.html",{"form":form})      


def search_book(request):
    form=searchform()
    if request.method=="POST":
      form=searchform(request.POST) 
      if form.is_valid():
         title=form.cleaned_data["title"]
         try:
             my_value=books_db.objects.get(title=title) 
         except books_db.DoesNotExist:
             return render(request,"books_app/error_book.html")
         return render(request,"books_app/result_book.html",context={"book":my_value})
      else:
         print(" error form invalid")
    return render(request,"books_app/search_book.html",{"form":form})
    
      

