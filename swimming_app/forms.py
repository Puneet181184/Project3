from django import forms
from swimming_app.models import swimming_db

class playerform(forms.ModelForm):
      class Meta():
         model=swimming_db
         fields=["name","age","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=swimming_db
         fields=["name","rank"] 
class detailsform(forms.ModelForm):
      class Meta():
         model=swimming_db
         fields=["name","medals"] 
class pointstatsform(forms.ModelForm):
      class Meta():
         model=swimming_db
         fields=["name","gold","silver","bronze"]   
class searchform(forms.ModelForm):
      class Meta():
         model=swimming_db
         fields=["name"]                  