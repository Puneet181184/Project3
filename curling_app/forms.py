from django import forms
from curling_app.models import curling_db

class playerform(forms.ModelForm):
      class Meta():
         model=curling_db
         fields=["name","age","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=curling_db
         fields=["name","ranking"] 

class searchform(forms.ModelForm):
      class Meta():
         model=curling_db
         fields=["name"]                                             