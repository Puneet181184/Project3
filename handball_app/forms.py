from django import forms
from handball_app.models import handball_db

class playerform(forms.ModelForm):
      class Meta():
         model=handball_db
         fields=["name","age","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=handball_db
         fields=["name","height","weight","position"] 
class searchform(forms.ModelForm):
      class Meta():
         model=handball_db
         fields=["name"]                                             