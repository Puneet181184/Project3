from django import forms
from taekwondo_app.models import taekwondo_db

class playerform(forms.ModelForm):
      class Meta():
         model=taekwondo_db
         fields=["name","age","dob","country"]