from django import forms
from tabletennis_app.models import tabletennis_db

class playerform(forms.ModelForm):
      class Meta():
         model=tabletennis_db
         fields=["name","age","dob","country"]