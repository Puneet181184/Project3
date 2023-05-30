from django import forms
from iceskating_app.models import iceskating_db

class playerform(forms.ModelForm):
      class Meta():
         model=iceskating_db
         fields=["name","age","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=iceskating_db
         fields=["name","height","weight"]  
class detailsform(forms.ModelForm):
      class Meta():
         model=iceskating_db
         fields=["name","level"]                         
class searchform(forms.ModelForm):
      class Meta():
         model=iceskating_db
         fields=["name"]              