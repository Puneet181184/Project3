from django import forms
from skating_app.models import skating_db

class playerform(forms.ModelForm):
      class Meta():
         model=skating_db
         fields=["name","age","dob"]
class aboutform(forms.ModelForm):
      class Meta():
         model=skating_db
         fields=["name","gender","club"]
class searchform(forms.ModelForm):
      class Meta():
         model=skating_db
         fields=["name"]                               
