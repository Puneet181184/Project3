from django import forms
from tabletennis_app.models import tabletennis_db

class playerform(forms.ModelForm):
      class Meta():
         model=tabletennis_db
         fields=["name","age","dob","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=tabletennis_db
         fields=["name","gender","rank","bestrank"]
class detailsform(forms.ModelForm):
      class Meta():
         model=tabletennis_db
         fields=["name","debut","height","weight"] 
class careerstatsform(forms.ModelForm):
      class Meta():
         model=tabletennis_db
         fields=["name","plays","grip"] 
class singlesstatsform(forms.ModelForm):
      class Meta():
         model=tabletennis_db
         fields=["name","singlesplayed","singleswon","singleslost"] 
class doublesstatsform(forms.ModelForm):
      class Meta():
         model=tabletennis_db
         fields=["name","doublesplayed","doubleswon","doubleslost"]
class totalstatsform(forms.ModelForm):
      class Meta():
         model=tabletennis_db
         fields=["name","totalplayed","totalwon","totallost"] 




