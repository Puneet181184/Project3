from django import forms
from biathlon_app.models import biathlon_db

class playerform(forms.ModelForm):
      class Meta():
         model=biathlon_db
         fields=["name","dob","country"]

class aboutform(forms.ModelForm):
      class Meta():
         model=biathlon_db
         fields=["name","gender","rank","points"]

class searchform(forms.ModelForm):
      class Meta():
         model=biathlon_db
         fields=["name"]            

                                             
