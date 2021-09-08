from django import forms
from badminton_app.models import badminton_db

class playerform(forms.ModelForm):
      class Meta():
         model=badminton_db
         fields=["name","age","dob","country"]