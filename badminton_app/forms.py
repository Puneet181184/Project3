from django import forms
from badminton_app.models import badminton_db

class playerform(forms.ModelForm):
      class Meta():
         model=badminton_db
         fields=["name","age","dob","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=badminton_db
         fields=["name","gender","rank","tourrank"] 
class detailsform(forms.ModelForm):
      class Meta():
         model=badminton_db
         fields=["name","debut","height","weight"] 
class careerstatsform(forms.ModelForm):
      class Meta():
         model=badminton_db
         fields=["name","plays","careerwins"]
class singlesstatsform(forms.ModelForm):
      class Meta():
         model=badminton_db
         fields=["name","singlesplayed","singleswon","singleslost"]
class doublesstatsform(forms.ModelForm):
      class Meta():
         model=badminton_db
         fields=["name","doublesplayed","doubleswon","doubleslost"] 
class mixedstatsform(forms.ModelForm):
      class Meta():
         model=badminton_db
         fields=["name","mixedplayed","mixedwon","mixedlost"]
class searchform(forms.ModelForm):
      class Meta():
         model=badminton_db
         fields=["name"]                                                         
                                                            