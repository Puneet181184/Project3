from django import forms
from fencing_app.models import fencing_db

class playerform(forms.ModelForm):
      class Meta():
         model=fencing_db
         fields=["name","age","dob","country"]