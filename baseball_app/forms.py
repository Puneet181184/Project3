from django import forms
from baseball_app.models import baseball_db

class playerform(forms.ModelForm):
      class Meta():
         model=baseball_db
         fields=["name","age","dob","nationality"]
class aboutform(forms.ModelForm):
      class Meta():
         model=baseball_db
         fields=["name","college","team","position"]
class detailsform(forms.ModelForm):
      class Meta():
         model=baseball_db
         fields=["name","debut","height","weight"]
class gamestatsform(forms.ModelForm):
      class Meta():
         model=baseball_db
         fields=["name","games","appearances","atbats"]  
class runstatsform(forms.ModelForm):
      class Meta():
         model=baseball_db
         fields=["name","runs","hits","doubles","triples","homeruns","runsbatted"] 
class strikestatsform(forms.ModelForm):
      class Meta():
         model=baseball_db
         fields=["name","steals","walks","strikeouts"]
class basestatsform(forms.ModelForm):
      class Meta():
         model=baseball_db
         fields=["name","stolenbases","caughtstealing","totalbases"]                                                   