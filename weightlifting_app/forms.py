from django import forms
from weightlifting_app.models import weightlifting_db

class playerform(forms.ModelForm):
      class Meta():
         model=weightlifting_db
         fields=["name","age","dob","country"]
