from django import forms
from rugby_app.models import rugby_db

class playerform(forms.ModelForm):
      class Meta():
         model=rugby_db
         fields=["name","age","dob","nationality"]