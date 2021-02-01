from django import forms
from tennis_app.models import tennis_db

class playerform(forms.ModelForm):
      class Meta():
         model=tennis_db
         fields=["name","age","dob","nationality"]
         
