from django import forms
from pool_app.models import pool_db

class playerform(forms.ModelForm):
      class Meta():
         model=pool_db
         fields=["name","age","dob","country"]