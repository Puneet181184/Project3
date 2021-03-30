from django import forms
from basketball_app.models import basketball_db

class playerform(forms.ModelForm):
      class Meta():
         model=basketball_db
         fields=["name","age","dob","nationality"]