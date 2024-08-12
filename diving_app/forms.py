from django import forms
from diving_app.models import diving_db

class playerform(forms.ModelForm):
      class Meta():
         model=diving_db
         fields=["name","dob","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=diving_db
         fields=["name","gender","discipline"] 
class searchform(forms.ModelForm):
      class Meta():
         model=diving_db
         fields=["name"]                                             