from django import forms
from kickboxing_app.models import kickboxing_db

class playerform(forms.ModelForm):
      class Meta():
         model=kickboxing_db
         fields=["name","age","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=kickboxing_db
         fields=["name","height","weight"] 
class pointstatsform(forms.ModelForm):
      class Meta():
         model=kickboxing_db
         fields=["name","wins","losses"] 
class searchform(forms.ModelForm):
      class Meta():
         model=kickboxing_db
         fields=["name"]            