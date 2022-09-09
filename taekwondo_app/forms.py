from django import forms
from taekwondo_app.models import taekwondo_db

class playerform(forms.ModelForm):
      class Meta():
         model=taekwondo_db
         fields=["name","age","dob","country"]
class aboutform(forms.ModelForm):
      class Meta():
         model=taekwondo_db
         fields=["name","gender","weight"]
class detailsform(forms.ModelForm):
      class Meta():
         model=taekwondo_db
         fields=["name","rank"]
class pointstatsform(forms.ModelForm):
      class Meta():
         model=taekwondo_db
         fields=["name","points"] 
class searchform(forms.ModelForm):
      class Meta():
         model=taekwondo_db
         fields=["name"]                                       