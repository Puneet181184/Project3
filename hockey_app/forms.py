from django import forms
from hockey_app.models import hockey_db

class playerform(forms.ModelForm):
      class Meta():
         model=hockey_db
         fields=["name","dob","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=hockey_db
         fields=["name","gender","height","weight"] 
class searchform(forms.ModelForm):
      class Meta():
         model=hockey_db
         fields=["name"]                                             