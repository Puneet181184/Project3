from django import forms
from paragliding_app.models import paragliding_db

class playerform(forms.ModelForm):
      class Meta():
         model=paragliding_db
         fields=["name","age","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=paragliding_db
         fields=["name","id","gender"] 
class searchform(forms.ModelForm):
      class Meta():
         model=paragliding_db
         fields=["name"]                                             