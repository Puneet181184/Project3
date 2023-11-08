from django import forms
from polo_app.models import polo_db

class playerform(forms.ModelForm):
      class Meta():
         model=polo_db
         fields=["name","age","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=polo_db
         fields=["name","status","points"] 
class searchform(forms.ModelForm):
      class Meta():
         model=polo_db
         fields=["name"]                                             