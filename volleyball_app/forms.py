from django import forms
from volleyball_app.models import volleyball_db

class playerform(forms.ModelForm):
      class Meta():
         model=volleyball_db
         fields=["name","age","dob","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=volleyball_db
         fields=["name","gender","rank"] 
class detailsform(forms.ModelForm):
      class Meta():
         model=volleyball_db
         fields=["name","height","weight"]  
class pointstatsform(forms.ModelForm):
      class Meta():
         model=volleyball_db
         fields=["name","points"] 
class searchform(forms.ModelForm):
      class Meta():
         model=volleyball_db
         fields=["name"]                                             