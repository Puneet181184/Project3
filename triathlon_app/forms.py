from django import forms
from triathlon_app.models import triathlon_db

class playerform(forms.ModelForm):
      class Meta():
         model=triathlon_db
         fields=["name","dob","country"]

class aboutform(forms.ModelForm):
      class Meta():
         model=triathlon_db
         fields=["name","gender","rank","wins"]

class searchform(forms.ModelForm):
      class Meta():
         model=triathlon_db
         fields=["name"]            

                                             
