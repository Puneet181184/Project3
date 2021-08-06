from django import forms
from golf_app.models import golf_db

class playerform(forms.ModelForm):
      class Meta():
         model=golf_db
         fields=["name","age","dob","country"]