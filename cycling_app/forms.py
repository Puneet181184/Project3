from django import forms
from cycling_app.models import cycling_db

class playerform(forms.ModelForm):
      class Meta():
         model=cycling_db
         fields=["name","age","dob","country"]