from django import forms
from cricket_app.models import cricket_db

class playerform(forms.ModelForm):
      class Meta():
         model=cricket_db
         fields=["name","age","country"] 