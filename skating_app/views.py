from django.shortcuts import render
from skating_app.models import skating_db
from skating_app.forms import playerform
from skating_app.forms import aboutform
from skating_app.forms import searchform

# Create your views here.
def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"skating_app/home.html")
