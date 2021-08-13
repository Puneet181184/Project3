from django import forms
from golf_app.models import golf_db

class playerform(forms.ModelForm):
      class Meta():
         model=golf_db
         fields=["name","age","dob","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=golf_db
         fields=["name","currentrank","bestrank"]
class detailsform(forms.ModelForm):
      class Meta():
         model=golf_db
         fields=["name","debut","height","weight"]
class gamestatsform(forms.ModelForm):
      class Meta():
         model=golf_db
         fields=["name","events","madecuts"] 
class positionstatsform(forms.ModelForm):
      class Meta():
         model=golf_db
         fields=["name","first","second","third","fourth"]
class pointstatsform(forms.ModelForm):
      class Meta():
         model=golf_db
         fields=["name","totalpoints","averagepoints","divisor"] 
class searchform(forms.ModelForm):
      class Meta():
         model=golf_db
         fields=["name"]                                                         


