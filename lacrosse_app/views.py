from django.shortcuts import render
from lacrosse_app.models import lacrosse_db
from lacrosse_app.forms import playerform
from lacrosse_app.forms import aboutform
from lacrosse_app.forms import detailsform
from lacrosse_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"lacrosse_app/home.html")
