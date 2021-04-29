from django import forms
from baseball_app.models import baseball_db

class playerform(forms.ModelForm):
      class Meta():
         model=baseball_db
         fields=["name","age","dob","nationality"]