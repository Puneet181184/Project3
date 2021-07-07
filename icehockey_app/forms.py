from django import forms
from icehockey_app.models import icehockey_db

class playerform(forms.ModelForm):
      class Meta():
         model=icehockey_db
         fields=["name","age","dob","nationality"]