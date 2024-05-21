from django import forms
from skiing_app.models import skiing_db

class playerform(forms.ModelForm):
      class Meta():
         model=skiing_db
         fields=["name","age","dob"]
class aboutform(forms.ModelForm):
      class Meta():
         model=skiing_db
         fields=["name","height","skitype"]
class searchform(forms.ModelForm):
      class Meta():
         model=skiing_db
         fields=["name"]                               
