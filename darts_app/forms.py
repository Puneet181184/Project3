from django import forms
from darts_app.models import darts_db

class playerform(forms.ModelForm):
      class Meta():
         model=darts_db
         fields=["name","age","dob","country"]