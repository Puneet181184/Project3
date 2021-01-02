from django import forms
from football_app.models import football_db

class playerform(forms.ModelForm):
      class Meta():
         model=football_db
         fields=["name","age","dob","nationality","birthplace"]
