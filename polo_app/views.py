from django.shortcuts import render
from polo_app.models import polo_db
from polo_app.forms import playerform
from polo_app.forms import aboutform
from polo_app.forms import detailsform
from polo_app.forms import searchform

def home(request):
	#return HttpResponse("Hello World!")
	return render(request,"polo_app/home.html")
def player(request):
    players_list=polo_db.objects.order_by("name")
    polo_dict={"player":players_list}
    return render(request,"polo_app/player.html",context=polo_dict)	